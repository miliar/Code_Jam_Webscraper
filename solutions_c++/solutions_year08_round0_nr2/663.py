#include <stdio.h>
#include <string.h>

// Estructura de un evento
typedef struct
{
    int newReadyTrainsA;
    int newReadyTrainsB;
    int trainsLeavingA;
    int trainsLeavingB;
}
Event;

// La lista de eventos del día, normalizada a minutos
Event eventList[1501];
// Los límites
int T, NA, NB;
// Trenes requeridos al inicio del día en A y en B
int reqTrainA, reqTrainB;


void InitEventList()
{
     // Inicializar la lista de eventos
     int i;
     
     for (i=0; i<1501; i++)
     {
         eventList[i].newReadyTrainsA = 0;
         eventList[i].newReadyTrainsB = 0;
         eventList[i].trainsLeavingA = 0;
         eventList[i].trainsLeavingB = 0;
     }
}

// Convierte a minuto normalizado una hora expresada en formato HH:MM
int ConvertToMinute(char *strTime)
{
    int hours, minutes;
    
    hours = ((strTime[0] - '0') * 10) + (strTime[1] - '0');
    minutes = ((strTime[3] - '0') * 10) + (strTime[4] - '0');
    
    return ( (hours*60) + minutes );
}

// Resolver el caso de prueba
void SolveCase()
{
     // Número de trenes disponibles en A y en B
     int curTrainA = 0, curTrainB = 0;
     int i;
     
     reqTrainA = 0;
     reqTrainB = 0;
     
     // Recorrer cada minuto del día para simular el comportamiento de los trenes
     for (i=0; i<1501; i++)
     {
         // Aumentar el número de trenes disponibles en A y en B de acuerdo a 
         // los nuevos trenes libres para partir en cada caso
         curTrainA += eventList[i].newReadyTrainsA;
         curTrainB += eventList[i].newReadyTrainsB;
         
         // Procesar los viajes que parten desde A, comparando contra el número
         // de trenes actuales
         if (eventList[i].trainsLeavingA != 0)
         {
             if (curTrainA >= eventList[i].trainsLeavingA)
                curTrainA -= eventList[i].trainsLeavingA;
             else
             {
                 // No hay trenes dispoibles para todos los viajes de A, debe
                 // aumentarse los requeridos de la mañana
                 reqTrainA += (eventList[i].trainsLeavingA - curTrainA);
                 curTrainA = 0;
             }
         }
         
         // Procesar los viajes que parten desde B, comparando contra el número
         // de trenes actuales
         if (eventList[i].trainsLeavingB != 0)
         {
             if (curTrainB >= eventList[i].trainsLeavingB)
                curTrainB -= eventList[i].trainsLeavingB;
             else
             {
                 // No hay trenes dispoibles para todos los viajes de A, debe
                 // aumentarse los requeridos de la mañana
                 reqTrainB += (eventList[i].trainsLeavingB - curTrainB);
                 curTrainB = 0;
             }
         }
     }
}

int main(int argc, char *argv[])
{
    FILE *inFile, *outFile;
    
    inFile = fopen("input.txt", "rt");
    outFile = fopen("output.txt", "wt");
    
    int numCases, i, j;
    char departureTime[10], arrivalTime[10];
    int minDepTime, minArrTime; // Tiempos de salida y llegada normalizados a minutos
    
    fscanf(inFile, "%d", &numCases);
    
    for (i=0; i<numCases; i++)
    {
        InitEventList();
        
        // Leer los datos de límites
        fscanf(inFile, "%d", &T);
        fscanf(inFile, "%d", &NA);
        fscanf(inFile, "%d", &NB);
        
        // Leer los eventos de salida de trenes desde A
        for (j=0; j<NA; j++)
        {
            fscanf(inFile, "%s", departureTime);
            fscanf(inFile, "%s", arrivalTime);
            
            minDepTime = ConvertToMinute(departureTime);
            minArrTime = ConvertToMinute(arrivalTime);
            
            // Aumentar los trenes que salen a una hora desde A
            eventList[minDepTime].trainsLeavingA += 1;
            
            // Aumentar los trenes que están listos para salir desde B, 
            // teniendo el tiempo de llegada del tren + el turnaround T.
            eventList[minArrTime+T].newReadyTrainsB += 1;
        }
        
        // Leer los eventos de salida de trenes desde B
        for (j=0; j<NB; j++)
        {
            fscanf(inFile, "%s", departureTime);
            fscanf(inFile, "%s", arrivalTime);
            
            minDepTime = ConvertToMinute(departureTime);
            minArrTime = ConvertToMinute(arrivalTime);
            
            // Aumentar los trenes que salen a una hora desde B
            eventList[minDepTime].trainsLeavingB += 1;
            
            // Aumentar los trenes que están listos para salir desde A,
            // teniendo el tiempo de llegada del tren + el turnaround T
            eventList[minArrTime+T].newReadyTrainsA += 1;
        }
        
        // Resolver el caso
        SolveCase();
        
        // Imprimir los resultados de mínimos requeridos para este caso
        fprintf(outFile, "Case #%d: %d %d\n", i+1, reqTrainA, reqTrainB);
    }
    
    fclose(inFile);
    fclose(outFile);
    return 0;
}
