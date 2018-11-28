#include<iostream>
using namespace std;
char a[4][4];
int win()
{
  int r[4]={0,0,0,0};
  int c[4]={0,0,0,0};
  int cross[2]={0,0};
  // X : 1 , O : -1
  for(int i = 0 ;i < 4 ; i++)
  {
    int t1,t2; t1 = t2 = 0;
    int t11,t22 ; t11 = t22 = 0;
    int extra = 0, extra2 = 0;
   for(int j = 0 ;j < 4 ; j++)
   {
	if(a[i][j] =='T')extra++;
	if(a[i][j] =='X')t1++;
	else if(a[i][j] =='O')t2++;
	
	if(a[j][i] =='T')extra2++;
	if(a[j][i]=='X')t11++;
	else if(a[j][i]=='O')t22++;
   }
	
   if(t1 + extra == 4)r[i] = 1;
   else if(t2 + extra == 4)r[i] = -1;
   if(t11 + extra2 == 4)c[i] = 1;
   else if( t22 + extra2 == 4)c[i] = -1;
  }
  for(int i = 0 ;i < 4 ; i++)
  {
	if(r[i])return r[i];
	else if(c[i])return c[i];
  }
 // cross line
 int OC = 0,XC = 0;
 for(int i = 0 ;i < 4 ; i++)
 {
        if(a[i][i] =='T'){OC++,XC++;}
	if(a[i][i] == 'O')OC++;
	else if(a[i][i] =='X')XC++;
 }
 if(OC == 4) return -1;
 else if(XC == 4) return 1;
 
 OC = XC = 0;
 for(int i = 0 ;i < 4 ; i++)
 {
        if(a[i][3-i] =='T'){OC++,XC++;}
	if(a[i][3-i] == 'O')OC++;
	else if(a[i][3-i] =='X')XC++;
 }
 if(OC == 4) return -1;
 else if(XC == 4) return 1;

}
int main()
{
	int ret,cas;
	cin>>cas;
	for(int q = 1;q<=cas ;q++)
	{
	
		int X, O;
		int dot = 0;
		X = O = 0;
	  for(int i = 0 ;i < 4 ; i++)
	   for(int j = 0 ;j < 4 ;j++)
	   {
	     cin>>a[i][j];
		if(a[i][j] =='.')dot++;
		if(a[i][j] =='O')O++;
		else if(a[i][j]=='X')X++;
  	   }
	   ret = win();
		cout<<"Case #"<<q<<": ";
	   if(ret == 1)	
		cout<<"X won"<<endl;
	   else if(ret == -1)
		cout<<"O won"<<endl;
	   else
	   {
		if(dot > 0) cout<<"Game has not completed"<<endl;
		else cout<<"Draw"<<endl;
	   }
	      
	}
	return 0;
}
