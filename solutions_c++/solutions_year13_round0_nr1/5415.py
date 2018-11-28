#include<iostream>
#include <stdio.h>

using namespace std;

int main()
{
     //freopen ("a.in","r",stdin);
     //freopen ("a.sal","w",stdout);
     int ganador[10] = {15,24,3840,61440,4369,8738,17476,34952,4680,33825};

    int n;
	
	cin>>n;
	
	for (int i = 0; i<n;i++)
	{
             char tablero;
             int tableroX = 0;
             int tableroO = 0;
             int jugadas = 0;
             cout<<"Case #"<<(i+1)<<": ";
	     for (int j=0; j<4; j++)
		 {  
		    for (int k=0;k<4;k++)
			{
			    tablero = '.';
 
			    cin>>tablero;
                            if (tablero != '.') jugadas++;
                            if (tablero == 'X' || tablero == 'T')
                            {
                                int tmp = 1;
                                tmp = tmp<<(4*j+k);
                                tableroX ^= tmp;                                
                            }
                            if (tablero == 'O' || tablero == 'T')
                            {
                                int tmp = 1;
                                tmp = tmp << (4*j+k);
                                //cout<<(4*j+k)<<" - "<<tmp<<endl;
                                tableroO ^= tmp;
                                //cout<<tableroO<<endl;                                
                            }
			}
		 }
          //cout<<"---------"<<endl;
           //cout<<tableroO<<" "<<tableroX<<endl;
           int i = 0;
           for (i = 0; i < 10; i++)
           {
               int tmp = tableroX & ganador[i];
               int unos = 0;
               while(tmp>0)
               {
                   if (tmp&1 > 0) unos++;
                   tmp = tmp >> 1;
                }
                if (unos == 4){
                    cout<<"X won"<<endl;
                    break;
                }
               tmp = tableroO & ganador[i];
               unos = 0;
               while(tmp>0)
               {
                   if (tmp&1 > 0) unos++;
                   tmp = tmp >> 1;
                }
                if (unos == 4){
                    cout<<"O won"<<endl;
                    break;
                }
           }
           if (i == 10 && jugadas == 16){
               cout<<"Draw"<<endl;
               }
               if (i == 10 && jugadas != 16){
               cout<<"Game has not completed"<<endl;
               }
	}
	
	fclose(stdin);
	fclose(stdout);
}