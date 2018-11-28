#include <cstdlib>
#include <iostream>
#include<fstream>
using namespace std;
char exist[100][100000];
int no=0;
void add(char *temp)
{
     int i,j=0,k;
     char str[10000],home[10000];
     strcpy(home,"");
     for(i=1;i<=strlen(temp);i++)
     {
                                if((temp[i]=='/')|(i==strlen(temp)))
                                {
                                                str[j]='\0';                   
                                                strcat(str,home);
                                                j=0;
                                                for(k=0;k<no;k++)
                                                                 if(strcmp(exist[k],str)==0)
                                                                                            break;
                                                if(k==no)
                                                {
                                                         strcpy(exist[no++],str);
                                                         //sprintf(exist[no++],"%s",str);
                                                     //    cout<<"Initial    "<<str<<"\t"<<exist[no-1];
                                                         }
                                                strcpy(home,str);
                                                continue;
                                }
                                str[j++]=temp[i];
     }
}
int main(int argc, char *argv[])
{
    int i,j,k,l,cno,x,count,n,m;
    char a[100][10000],b[100][10000],str[10000],home[10000]="";
    ifstream fin("input.txt");
    ofstream fout("output.txt");
    for(fin>>count,cno=0;cno<count;cno++)
    {
                                         fin>>n>>m;
                                         no=0;
                                         for(i=0;i<n;i++)
                                         {
                                                         fin>>a[i];
                                                         add(a[i]);
                                         }
                                         x=0;
                                         for(i=0;i<m;i++)
                                         {
                                                         fin>>b[i];      
                                                         k=0;                                   
                                                         strcpy(home,"");
                                                         for(j=1;j<=strlen(b[i]);j++)
                                                         {
                                                                                    if((b[i][j]=='/')|(j==strlen(b[i])))
                                                                                    {
                                                                                                    str[k]='\0';
                                                                                                    strcat(str,home);
                                                                                                    k=0;
                                                                                                    for(l=0;l<no;l++)
                                                                                                                     if(strcmp(exist[l],str)==0)
                                                                                                                                                break;
                                                                                                    if(l==no)
                                                                                                    {
                                                                                                             //cout<<str<<"   Notfound\n";
                                                                                                             sprintf(exist[no++],"%s",str);
                                                                                                             //cout<<exist[no-1]<<endl;
                                                                                                             x++;
                                                                                                    }
                                                                                                    strcpy(home,str);
                                                             //                                       level++;
                                                                                                    continue;
                                                                                    }
                                                                                    str[k++]=b[i][j];
                                                         }
                                         }
                                         //for(i=0;i<no;i++)
                                           //               cout<<exist[i]<<endl;
                                         cout<<"Answer is "<<x<<endl;
                                         fout<<"Case #"<<cno+1<<": "<<x<<endl;
    }
    system("PAUSE");
    return EXIT_SUCCESS;
}
