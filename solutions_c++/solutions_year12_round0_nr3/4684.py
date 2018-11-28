#include<iostream.h>
#include<fstream.h>
#include<conio.h>
int main()
{   
    ifstream file;
    file.open("input2.txt");
    int T,A[50],B[50],count=0,ch,ch1,ch2,ch3,ch4,c1,c2,s[50],i;
    while(!file.eof())
    {file>>T;
    for(i=0;i<T;i++)
    {
    file>>A[i];
    file>>B[i];
     }
     for(i=0;i<T;i++)
    { count=0;
      if((B[i]/100)==0)
      ch=2;
      else if(B[i]/10==0)
      ch=1;
      else 
      ch=3;
                    for(int j=A[i];j<B[i];j++)
                    { if(ch==3)
                           { ch1=j%10;
                            ch2=j%100;
                            ch3=j/10;
                            ch4=j/100;
                            c1=(ch1*100)+ch3;
                            c2=(ch2*10)+ch4;
                            if(c1>A[i]&&c1<=B[i])
                            {count++;
                            //cout<<c1<<endl;
                            }
                            if(c2>A[i]&&c2<=B[i])
                            {//cout<<c2<<endl;
                            count++;
                            }A[i]++;
                            }
                     else if(ch==2)
                           {ch1=j%10;
                            ch3=j/10;
                            c1=(ch1*10)+ch3;
                            {if(c1>A[i]&&c1<B[i])
                            //cout<<c1<<endl;
                            count++;}
                            //if(c2>A[i]&&c2<B[i])
                            //count++;
                            A[i]++;
                            }
                            else
                            count=0;
                            }
                     
                            s[i]=count;
                            }
      for(i=0;i<T;i++)
      {
                      cout<<"Case #"<<i+1<<": "<<s[i];
                      cout<<"\n";
      }
      getch();
      
                    
    
    return 0;
}
}
