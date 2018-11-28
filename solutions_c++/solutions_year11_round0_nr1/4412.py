#include<iostream>
#include<stdio.h>
#include<fstream>
#include<conio.h>
using namespace std;
   int o[110][2];
        int b[110][2];
int main()
{
    //printf("asdasd");
    int t;
    ofstream f1 ("new.txt");
           //  o=[0,0];
    scanf("%d",&t);
    int max=t;
    do
    {
        int n;
        int ubo=-1;
        int ubb=-1;
        scanf("%d",&n);
        for(int q=0;q<111;q++)
        {
        o[q][0]=0;
        o[q][1]=0;
        b[q][0]=0;
        b[q][1]=0;
      }
        //  o[100][2]=0;
       // b[100][2]=0;
                           
        for(int q=1;q<=n;q++)
        {
                char ch;
        cin>>ch;
        if(ch==79)
        {
              ubo++;
              scanf("%d",&o[ubo][0]);
              o[ubo][1]=q;
        }
        else
        {
            ubb++;
            scanf("%d",&b[ubb][0]);
            b[ubb][1]=q;
        }        
        }
        int peak=1;
         int ctu=1,ctb=1;
       int countu=0,countb=0;
       int cttu=0,cttb=0;
        do
        {
        int flag=0;
        int flag2=0;
      
       if(ctu < o[cttu][0])
       {      ctu++;
             countu++;
       }
      else if(ctu > o[cttu][0])
       {      ctu--;
             countu++;
       }
      else if(ctu == o[cttu][0])
       {      
          if(o[cttu][1]==peak)
          {   countu++;
             cttu++;
             //ctu++;
             //peak++;
             flag=1;
             }
             else
             {
                countu++; 
                 
             }
       } 
       //cout<<endl;
   //  cout<<countu<<" "<<ctu<<" "<<peak<<endl;
 //     getch();
 
       
       if(ctb < b[cttb][0])
       {      ctb++;
             countb++;
       }
      else if(ctb > b[cttb][0])
       {      ctb--;
             countb++;
       }
       else if(ctb == b[cttb][0])
       {      
          if(b[cttb][1]==peak)
          {   countb++;
             cttb++;
            // ctb++;
             //peak++;
             flag2=1;
             }
             else
             {
                countb++; 
                 
             }
       }
       
            if(flag==1)
                       peak++;
                       
                       if(flag2==1)
                                   peak++;
       
        
                
                }while(peak!=n+1);
        
  //      cout<<endl<<countu<<endl;
        
//  cout<<countb<<" "<<ctb<<" "<<peak<<endl;
        
        
        
          f1<<"Case #"<<max-t+1<<": "<<countu<<endl;
        t--;
    }while(t!=0);
  
    //getch();
    f1.close();
    return 0;
    
}
