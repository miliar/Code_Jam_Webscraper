#include<iostream>
#include<fstream>
#include<cstring>


using namespace std;
char ans[10000];
char pa[200][5],opp[200][5];
char str[200];
long long N1,N2,N3;
char li[200];

void solution()
{
     int pr=-1;
     int flag=0;
     int i,j,k;
    for(i=0;i<N3;i++)
    {
                     flag=0;
                     for(j=0;j<N1;j++)
                                              {
                                                        if(pa[j][0]==pa[j][1] )
                                                        {
                                                                              if(str[i]==pa[j][0])
                                                                              {
                                                                                str[++pr]=pa[j][2];
                                                                                flag=1;
                                                                                break;
                                                                              }  
                                                        }
                                               }
                     if(flag==0)
                     {
                              if(pr!=-1)
                              {
                                        if(str[pr]=='Q'|| str[pr]=='W'|| str[pr]=='E'||str[pr]=='R' ||str[pr]=='A'||str[pr]=='S'||str[pr]=='D'||str[pr]=='F')       
                                        {
                                              for(j=0;j<N1;j++)
                                              {
                                                        
                                                              if((str[i]==pa[j][0] && str[pr]==pa[j][1]) || (str[i]==pa[j][1] && str[pr]==pa[j][0]))
                                                              {
                                                                  str[pr]=pa[j][2];
                                                                  flag=1;
                                                                  break;
                                                              }
                                                             
                                               }       
                                               if(flag==0) 
                                               {
                                                   for(j=0;j<N2;j++)
                                                   {
                                                                                            
                                                            for(k=0;k<=pr;k++)
                                                            {
                                                                 if((str[i]==opp[j][0] && str[k]==opp[j][1]) || (str[i]==opp[j][1] && str[k]==opp[j][0]))
                                                                 {
                                                                       pr=-1;
                                                                       flag=1;
                                                                       break;
                                                                 }
                                                            }
                                                        
                                                        if(flag==1)
                                                        break;
                               
                               
                                                   }
                                               }
                                         }      
                              }
                              
                     }        
                     if(flag==0)
                     {
                                         
                                          str[++pr]=str[i];
                     }
                     
    }

    ans[0]='[';
    int pp=1;
    for(i=0;i<pr;i++)
    {
         ans[pp++]=str[i];
         ans[pp++]=',';
         ans[pp++]=' ';            
    }
    if(pr>=0)
    {
            ans[pp++]=str[pr];
    }
    ans[pp++]=']';
    ans[pp]='\0';
    
}

int main()
{
    ifstream fin;
    ofstream fout;
    fin.open("input.txt");
    fout.open("output.txt");
    int T;
    fin>>T;
    int i,j;
    for(i=0;i<T;i++)
    {
                    fin>>N1;
                    //fout<<N1<<" ";
                    for(j=0;j<N1;j++)
                    {
                                    fin>>pa[j];                                   
                     //               fout<<pa[j]<<" ";
                    }
                    fin>>N2;
                     //fout<<N2<<" ";
                    for(j=0;j<N2;j++)
                    {
                                     fin>>opp[j];
                       //              fout<<opp[j]<<" ";
                    }
                    fin>> N3>>str;
                    //fout<<N3<<" "<<str<<"\n";
                   solution();

                    fout<<"Case #"<<i+1<<": "<<ans<<"\n";
                    cout<<"Case #"<<i+1<<": "<<ans<<"\n";
    }
    fin.close();
    fout.close();
    cin>>i;
    return 0;
}
