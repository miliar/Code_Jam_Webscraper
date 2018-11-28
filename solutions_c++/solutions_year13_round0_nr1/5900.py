#include <algorithm>
#include <map>
#include <string>
#include <assert.h>
#include <iostream>
using namespace std;

bool XWin,OWin,HasEmpty;
char mar[4][4];

void go(int i,int j,int iAdd,int jAdd, int step)
{	
	int XNum = 0;
	int ONum =0;
	int DotNum = 0;
	int TNum = 0;
	while(step--)
	{
		switch(mar[i][j])
		{
		case 'X': XNum ++; break;
		case 'O': ONum++;break;
		case '.':DotNum++;break;
		case 'T':TNum++;break;
		default:break;
		}

		i += iAdd;
		j+=jAdd;
	}

	if(DotNum !=0) HasEmpty = true;
	if((XNum == 3 && TNum == 1) || XNum == 4) {XWin = true;return;}
	if((ONum == 3 && TNum ==1) || ONum == 4 ) {OWin = true;return;}
	return;
}
int Ckeck()
{
	if(XWin) return 1;
	if(OWin) return 2;
	return 0;
}

int main()
{
	freopen("1.in","r",stdin);
  freopen("1.out","w",stdout);
	int t;
	
    scanf("%d\n",&t);
   
    for (int i=1;i<=t;i++)
    {       
		memset(mar,0,sizeof(mar));
		for(int j=0;j<4;j++)
		{
         gets(mar[j]);
		 //scanf("%4s",&mar[j]);
		}
		char str[3];
		gets(str);
		XWin = false;
		OWin = false;
		HasEmpty = false;
		
		//|
		go(0,0,0,1,4);
		if(Ckeck() != 0) goto end;

		go(1,0,0,1,4);
		if(Ckeck() != 0) goto end;

		go(2,0,0,1,4);
		if(Ckeck() != 0) goto end;

		go(3,0,0,1,4);
		if(Ckeck() != 0) goto end;

		//-
		go(0,0,1,0,4);
		if(Ckeck() != 0) goto end;

		go(0,1,1,0,4);
		if(Ckeck() != 0) goto end;

		go(0,2,1,0,4);
		if(Ckeck() != 0) goto end;

		go(0,3,1,0,4);
		if(Ckeck() != 0) goto end;

		///
		go(0,3,1,-1,4);
		if(Ckeck() != 0) goto end;

		//\ 
		go(0,0,1,1,4);
		if(Ckeck() != 0) goto end;

end:
         cout<<"Case #"<<i<<": ";
         if(XWin) cout<<"X won";
		 else if(OWin) cout<<"O won";
		 else if(HasEmpty) cout<<"Game has not completed";
		 else cout<<"Draw";
		 cout<<endl;
    }    

    return 1;
}