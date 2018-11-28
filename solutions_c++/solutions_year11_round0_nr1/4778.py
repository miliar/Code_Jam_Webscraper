#include <cstdlib>
#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char *argv[])
{
    int T,N;
    char color;
    int pos,robot;
    ifstream input ("A-large.in");
    ofstream output ("output.txt");
    input >> T;
    for(int line=0; line<T; line++)
    {
            input >> N;
            int buttons[N][2];
            int pozycja[2]={1,1};
            int cel[2]={-1,-1};
            for(int j=0; j<N; j++)
            {
                    input >> color;
                    input >> pos;
                    robot=(color=='O') ? 0 : 1;
                    if(cel[robot]==-1)cel[robot]=j;
                    buttons[j][0]=robot;
                    buttons[j][1]=pos;
            }            
            int time,pres=0;
            bool presed;
            //cout << "Czas \t| Orange \t| Blue" << endl;
            for(time=1; ; time++)
            {
                //cout << time << " \t| ";
                presed=false;
                for(int R=0; R<=1; R++)
                {
                    if(cel[R]!=-1)
                    {
                        if(pozycja[R]==buttons[cel[R]][1])
                        {
                            if(!presed&&pres==cel[R])
                            {
                                pres++;
                                presed=true;
                                cel[R]=-1;
                                for(int i=pres; i<N; i++)
                                {
                                    if(buttons[i][0]==R)
                                    {
                                        cel[R]=i;
                                        break;
                                    }
                                }
                                //cout << "Wcisnieto " << pozycja[R];
                            }
                            else
                            {
                                //cout << "Stoj na " << pozycja[R];
                            }                
                        }      
                        else
                        {
                            if(pozycja[R]<buttons[cel[R]][1])pozycja[R]++;
                            else if(pozycja[R]>buttons[cel[R]][1])pozycja[R]--;
                            //cout << "Idz do " << pozycja[R];
                        }        
                    }        
                    else
                    {
                        //cout << "Stoj na " << pozycja[R]; 
                    }
                    //if(R==0)cout << " \t| ";
                }
                //cout << endl;
                if(pres==N)break;
            }
            char buffer[255];
            sprintf(buffer,"Case #%d: %d",line+1,time);
            output << buffer;
            if(line!=T-1)output << endl;
            cout << buffer << endl;;
    }       
    input.close();
    output.close();
    //cout << "Czas generowania skryptu: " << clock()/CLOCKS_PER_SEC << " sekund" << endl;
    system("PAUSE");
    return EXIT_SUCCESS;
}
