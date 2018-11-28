#include<iostream.h>
#include<fstream.h>
#include<conio.h>
int main()
{   
    ifstream input;
    input.open("inputest.txt");
    int test,num1[50],num2[50],count=0,choice,case1,case2,case3,case4,a,b,cnt[50],i;
    while(!input.eof())
    {input>>test;
    for(i=0;i<test;i++)
    {
    input>>num1[i];
    input>>num2[i];
     }
     for(i=0;i<test;i++)
    { count=0;
      if((num2[i]/100)==0)
      choice=2;
      else if(num2[i]/10==0)
      choice=1;
      else 
      choice=3;
                    for(int j=num1[i];j<num2[i];j++)
                    { if(choice==3)
                           { case1=j%10;
                            case2=j%100;
                            case3=j/10;
                            case4=j/100;
                            a=(case1*100)+case3;
                            b=(case2*10)+case4;
                            if(a>num1[i]&&a<=num2[i])
                            count++;
                            
                            if(b>num1[i]&&b<=num2[i])
                            {
                            count++;
                            }
                            num1[i]++;
                            }
                     else if(choice==2)
                           {
                                   case1=j%10;
                            case3=j/10;
                            a=(case1*10)+case3;
                            {
                            if(a>num1[i]&&a<num2[i])
                            count++;
                            }
                            num1[i]++;
                            }
                            else
                            count=0;
                            }
                     
                            cnt[i]=count;
                            }
      for(i=0;i<test;i++)
      {
                      cout<<"Case #"<<i+1<<": "<<cnt[i];
                      cout<<"\n";
      }
      getch();
      
                    
    
    return 0;
}
}
