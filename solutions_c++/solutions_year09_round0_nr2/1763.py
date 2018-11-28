#include <stdio.h>
#include <conio.h>

int minorAround(int cell);
void resetMap();

int floods(int cell, char basis);
void getFloodInto(int cell);

void getFloodFrom(int cell);

int posNorth(int cell);
int posSouth(int cell);
    int posWest(int cell);
        int posEast(int cell);
            int posVertical(int cell);
                int posHorizontal(int cell);


int maxAltitude = 10000;
int maxCells = 10000;
char basis[26] = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};


int cellAltitude[10000];
int height, width;
char cellBasis[10000];
int floodsInto[10000];
int floodsFrom[10000][4];

int main(){
     FILE *fileIn, *fileOut;

	char linea[150];
	
	int i;
    int numMaps;
    
	fileIn=fopen("C:\\GCJ\\Q\\B-large.in", "r");
	fileOut=fopen("C:\\GCJ\\Q\\B-large.out", "w");
	if (fileIn!=NULL) {
     
        fscanf(fileIn,"%d\n",&numMaps);
        for (int iCase=0;iCase<numMaps;iCase++){
            resetMap();
    
            fscanf(fileIn,"%d %d\n",&height,&width);
    
            for (int iVertical=0;iVertical<height;iVertical++){
                for (int iHorizontal=0;iHorizontal<width;iHorizontal++){
                    fscanf(fileIn,"%d",cellAltitude+iVertical*width+iHorizontal);
                }
                fscanf(fileIn,"\n");
            }
            for (int i=0;i<(width*height);i++){
                getFloodInto(i);
            }
     
     
            for (int i=0;i<(width*height);i++){
                getFloodFrom(i);
            }
            int iBasisCount = 0;
            for (int i=0;i<(width*height);i++){
                iBasisCount = iBasisCount+floods(i,basis[iBasisCount]);
            }
     
            fprintf(fileOut,"Case #%d:\n",iCase+1); 
            for (int i=0;i<(width*height);i++){
                if (posHorizontal(i)!=(width-1))
                   fprintf(fileOut,"%c ",cellBasis[i]); 
                else
                   fprintf(fileOut,"%c\n",cellBasis[i]); 
            }            
                  
        }
     }
    fclose(fileIn);
    fclose(fileOut);
    return 0;  
}


int minorAround(int cell){
    int minorAltitude = cellAltitude[cell];
    int resCell = -1;
    int iPosNorth = posNorth(cell);
    if (iPosNorth!=-1 && cellAltitude[iPosNorth]<minorAltitude){
       minorAltitude = cellAltitude[iPosNorth];
       resCell = iPosNorth;
    }

    int iPosWest = posWest(cell);
    if (iPosWest!=-1 && cellAltitude[iPosWest]<minorAltitude){
       minorAltitude = cellAltitude[iPosWest];
       resCell = iPosWest;
    }

    int iPosEast = posEast(cell);
    if (iPosEast!=-1 && cellAltitude[iPosEast]<minorAltitude){
       minorAltitude = cellAltitude[iPosEast];
       resCell = iPosEast;
    }
    int iPosSouth = posSouth(cell);
    if (iPosSouth!=-1 && cellAltitude[iPosSouth]<minorAltitude){
       minorAltitude = cellAltitude[iPosSouth];
       resCell = iPosSouth;
    }

    return resCell;
}


int floods(int cell, char basis){
     if (cellBasis[cell]=='0'){
        cellBasis[cell] = basis;
        if (floodsInto[cell]!= -1)
           floods(floodsInto[cell], basis);
        for (int i=0;i<4;i++){
            if (floodsFrom[cell][i]!=-1)
               floods(floodsFrom[cell][i],basis);
        }
        return 1;
     }else return 0;
          
}

void resetMap(){
     for (int i=0;i<maxCells;i++){
         floodsInto[i]=-1;
         floodsFrom[i][0] = -1;
         floodsFrom[i][1] = -1;
         floodsFrom[i][2] = -1;
         floodsFrom[i][3] = -1;
         cellBasis[i] = '0';
         cellAltitude[i]=-1;
         width=0;
         height=0;
     }
}

void getFloodInto(int cell){
       floodsInto[cell] =  minorAround(cell);
}

void getFloodFrom(int cell){

    if (posNorth(cell)!=-1 && floodsInto[posNorth(cell)] == cell)
       floodsFrom[cell][0] = posNorth(cell);
    else floodsFrom[cell][0] = -1;
    if (posEast(cell)!=-1 && floodsInto[posEast(cell)] == cell)
       floodsFrom[cell][1] = posEast(cell);
        else floodsFrom[cell][1] = -1;
    if (posSouth(cell)!=-1 && floodsInto[posSouth(cell)] == cell)
       floodsFrom[cell][2] = posSouth(cell);
        else floodsFrom[cell][2] = -1;
    if (posWest(cell)!=-1 && floodsInto[posWest(cell)] == cell)
       floodsFrom[cell][3] = posWest(cell);
    else floodsFrom[cell][3] = -1;
}





int posNorth(int cell){
    if (posVertical(cell)>0)
       return cell-width;
    else return -1;
}

int posEast(int cell){
    if (posHorizontal(cell)<(width-1))
       return cell+1;
    else return -1;
}

int posSouth(int cell){
    if (posVertical(cell)<(height-1))
       return cell+width;
    else return -1;
}

int posWest(int cell){
    if (posHorizontal(cell)>0)
       return cell-1;
    else return-1;
}

int posHorizontal(int cell){
    return cell%width;
}

int posVertical(int cell){
    return cell/width;
}
