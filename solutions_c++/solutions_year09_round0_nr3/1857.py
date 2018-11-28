#include <iostream> 
#include <fstream> 
#include <string> 
#include <iomanip>

using namespace std;

const char file_in[] = "C-small-attempt0.in";
const char file_out[] = "C-small-attempt0.out";

int N = 0;
int counter = 0;
#define LENGTH 19

char teststring[1024] = {0};
char welcome[LENGTH+1] = {"welcome to code jam"};
int position = 0;
int pos[19] = {0};


int main()
{
    ofstream output; 
    string test;
    
    FILE *fp = fopen( file_in, "r");
    output.open(file_out);

    int tempfilepos = 0;

    while((teststring[tempfilepos] = fgetc(fp) ) != '\n' && teststring[tempfilepos] != EOF)
    {
        tempfilepos++;
    }
    N = atol(teststring);

    for(int n=0; n<N; n++)
    {
        //int tempfilepos = 0;
        memset(teststring, 0, 501);
        tempfilepos = 0;

        while((teststring[tempfilepos] = fgetc(fp) ) != '\n' && teststring[tempfilepos] != EOF)
        {
            tempfilepos++;
        }
        
        int len = tempfilepos;
        position = 0;
        counter = 0;
        for(int i=0; i<len; i++)
        {
            if( len < 19 )
            {
                break;
            }
            if(teststring[i] == welcome[0])
                position = i;

            break;
        }
        
        
        for(pos[0] = position; pos[0] < len; pos[0]++ )
        {
            if(teststring[pos[0]] == welcome[0])
                for(pos[1] = pos[0]+1; pos[1]< len; pos[1]++ )
                {
                    if(teststring[pos[1]] == welcome[1])
                        for(pos[2] = pos[1]+1; pos[2]< len; pos[2]++ )
                        {
                            if(teststring[pos[2]] == welcome[2])
                                for(pos[3] = pos[2]+1; pos[3]< len; pos[3]++ )
                                {
                                    if(teststring[pos[3]] == welcome[3])
                                        for(pos[4] = pos[3]+1; pos[4]< len; pos[4]++ )
                                        {
                                            if(teststring[pos[4]] == welcome[4])
                                                for(pos[5] = pos[4]+1; pos[5]< len; pos[5]++ )
                                                {
                                                    if(teststring[pos[5]] == welcome[5])
                                                        for(pos[6] = pos[5]+1; pos[6]< len; pos[6]++ )
                                                        {
                                                            if(teststring[pos[6]] == welcome[6])
                                                                for(pos[7] = pos[6]+1; pos[7]< len; pos[7]++ )
                                                                {
                                                                    if(teststring[pos[7]] == welcome[7])
                                                                        for(pos[8] = pos[7]+1; pos[8]< len; pos[8]++ )
                                                                        {
                                                                            if(teststring[pos[8]] == welcome[8])
                                                                                for(pos[9] = pos[8]+1; pos[9]< len; pos[9]++ )
                                                                                {
                                                                                    if(teststring[pos[9]] == welcome[9])
                                                                                        for(pos[10] = pos[9]+1; pos[10]< len; pos[10]++ )
                                                                                        {
                                                                                            if(teststring[pos[10]] == welcome[10])
                                                                                                for(pos[11] = pos[10]+1; pos[11]< len; pos[11]++ )
                                                                                                {
                                                                                                    if(teststring[pos[11]] == welcome[11])
                                                                                                        for(pos[12] = pos[11]+1; pos[12]< len; pos[12]++ )
                                                                                                        {
                                                                                                            if(teststring[pos[12]] == welcome[12])
                                                                                                                for(pos[13] = pos[12]+1; pos[13]< len; pos[13]++ )
                                                                                                                {
                                                                                                                    if(teststring[pos[13]] == welcome[13])
                                                                                                                        for(pos[14] = pos[13]+1; pos[14]< len; pos[14]++ )
                                                                                                                        {
                                                                                                                            if(teststring[pos[14]] == welcome[14])
                                                                                                                                for(pos[15] = pos[14]+1; pos[15]< len; pos[15]++ )
                                                                                                                                {
                                                                                                                                    if(teststring[pos[15]] == welcome[15])
                                                                                                                                        for(pos[16] = pos[15]+1; pos[16]< len; pos[16]++ )
                                                                                                                                        {
                                                                                                                                            if(teststring[pos[16]] == welcome[16])
                                                                                                                                                for(pos[17] = pos[16]+1; pos[17]< len; pos[17]++ )
                                                                                                                                                {
                                                                                                                                                    if(teststring[pos[17]] == welcome[17])
                                                                                                                                                        for(pos[18] = pos[17]+1; pos[18]< len; pos[18]++ )
                                                                                                                                                        {
                                                                                                                                                            if(teststring[pos[18]] == welcome[18])
                                                                                                                                                                counter++;
                                                                                                                                                        }   
                                                                                                                                                }
                                                                                                                                        }
                                                                                                                                        
                                                                                                                                }
                                                                                                                        }
                                                                                                                }
                                                                                                        }
                                                                                                }
                                                                                        }
                                                                                }
                                                                                
                                                                        }
                                                                }
                                                        }
                                                }
                                        }
                                }
                                
                        }
                }
        }
        //cout<<setfill('0')<<setw(4)<<counter%10000<<endl;
        output<<"Case #"<<n+1<<": ";
        output<<setfill('0')<<setw(4)<<counter%10000<<endl;
        
}
fclose(fp);
output.close();

//system("PAUSE");
return 0;
}
