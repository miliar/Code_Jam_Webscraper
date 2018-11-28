#include<iostream>
#include<stdio.h>
#include<fcntl.h>
#include<string.h>
using namespace std;
int main()
{
    int cases;
    char s[3502];
    unsigned long long int d[20];
    cin>>cases;
    gets(s);
    for(int cas=0;cas<cases; cas++)
    {
                gets(s);
                memset(d,0,sizeof(d));
                for(int i=0;i<strlen(s);i++)
                {
                        //cout<<s[i];
                        //for(int j=0;j<20;j++)
                        //{
                        //cout<<d[j]<<"\t";        
                       // }
                        switch(s[i])
                        {
                                    case 'w':
                                         d[0]++;
                                         break;
                                    case 'e':
                                         d[1]+=d[0];
                                         d[6]+=d[5];
                                         d[14]+=d[13];
                                         break;
                                    case 'l':
                                         d[2]+=d[1];
                                         break;
                                    case 'c':
                                         d[3]+=d[2];
                                         d[11]+=d[10];
                                         break;
                                    case 'o':
                                         d[4]+=d[3];
                                         d[9]+=d[8];
                                         d[12]+=d[11];
                                         break;
                                    case 'm':
                                         d[5]+=d[4];
                                         d[18]+=d[17];
                                         break;
                                    case 32:
                                         d[7]+=d[6];
                                         d[10]+=d[9];
                                         d[15]+=d[14];
                                         break;
                                    case 't':
                                         d[8]+=d[7];
                                         break;
                                    case 'd':
                                         d[13]+=d[12];
                                         break;
                                    case 'j':
                                         d[16]+=d[15];
                                         break;
                                    case 'a': 
                                         d[17]+=d[16];
                                         break;
                        }   
                        //cout<<endl;                           
                               
                }
                
                cout<<"Case #"<<cas+1<<": ";
                printf("%04llu",d[18]);
                if(cas!=cases-1) printf("\n");
                
            
    }    
}
