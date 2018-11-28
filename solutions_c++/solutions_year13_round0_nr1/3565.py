#include<iostream>
#include<string.h>

using namespace std;

/*
int check(int i)
{
	if(ch[i][j]==ch[i][j+1]) &&  (ch[i][j]==ch[i][j+2]) && (ch[i][j]==ch[i][j+3]) && (ch[i][j]=='X') ans=1;
	
	else if(ch[i][j]==ch[i][j+1]) &&  (ch[i][j]==ch[i][j+2]) && (ch[i][j]==ch[i][j+3]) && (ch[i][j]=='0') ans=2;
	
	else if(ch[i][j]==ch[i+1][j]) &&  (ch[i][j]==ch[i+2][j]) && (ch[i][j]==ch[i+3][j]) && (ch[i][j]=='X') ans=1;
	
	else if(ch[i][j]==ch[i][j+1]) &&  (ch[i][j]==ch[i][j+2]) && (ch[i][j]==ch[i][j+3]) && (ch[i][j]=='0') ans=2;
	
	else if(ch[i][j]==ch[i+1][j+1]) &&  (ch[i][j]==ch[i+2][j+2]) && (ch[i][j]==ch[i+3][j+3]) && (ch[i][j]=='X') ans=1;
	
	else if(ch[i][j]==ch[i][j+1]) &&  (ch[i][j]==ch[i][j+2]) && (ch[i][j]==ch[i][j+3]) && (ch[i][j]=='0') ans=2;
	
	else if(ch[i][j]==ch[i][j+1]) &&  (ch[i][j]==ch[i][j+2]) && (ch[i][j]==ch[i][j+3]) && (ch[i][j]=='0') ans=2;
	
}
*/
int main()
{

	int i,j,k,n,c,m,t,dot,x,z,ans;
	char ch[10][10];
	
	cin>>n;
	
	for(k=1;k<=n;k++) {
		dot=0;ans=0;
		
		for(i=1;i<=4;i++)
			for(j=1;j<=4;j++) {
			cin>>ch[i][j];
			if(ch[i][j]=='.') dot++;
			}
			getchar();
	//Row
	for(i=1;i<=4;i++) {
		t=0;z=0;x=0;
		for(j=1;j<=4;j++) {
			if(ch[i][j]=='X') x++;
			if(ch[i][j]=='O') z++;
			if(ch[i][j]=='T') t++;
		  }
				if(x==4 || (x==3 && t==1)) { ans=1; break;}
				if(z==4 || (z==3 && t==1)) { ans=2; break;}
	    }
	//Column
	if(ans==0) 
	for(i=1;i<=4;i++) {
		t=0;z=0;x=0;
		for(j=1;j<=4;j++) {
			if(ch[j][i]=='X') x++;
			if(ch[j][i]=='O') z++;
			if(ch[j][i]=='T') t++;
		  }
				if(x==4 || (x==3 && t==1)) { ans=1; break;}
				if(z==4 || (z==3 && t==1)) { ans=2; break;}
	    }
	//Left Diagonal
	t=0;x=0;z=0;
	if(ans==0) 
	for(i=1;i<=4;i++) {
			
			if(ch[i][i]=='X') x++;
			if(ch[i][i]=='O') z++;
			if(ch[i][i]=='T') t++;
			}
				if(x==4 || (x==3 && t==1)) { ans=1; }
				if(z==4 || (z==3 && t==1)){ ans=2; }
	 //   cout<<x<<"O: "<<z<<" t: "<<t<<endl;
	//Right Diagonal
	t=0;z=0;x=0;
	if(ans==0) 
	for(i=1;i<=4;i++) {
			if(ch[i][5-i]=='X') x++;
			if(ch[i][5-i]=='O') z++;
			if(ch[i][5-i]=='T') t++;	
		  }
				if(x==4 || (x==3 && t==1)) { ans=1; }
				if(z==4 || (z==3 && t==1)) { ans=2; }
	    

			if(ans==1) { cout<<"Case #"<<k<<": X won"<<endl; }
			 else if(ans==2) { cout<<"Case #"<<k<<": O won"<<endl; }
			  else if(dot>0) { cout<<"Case #"<<k<<": Game has not completed"<<endl; }
			   else { cout<<"Case #"<<k<<": Draw"<<endl; }
	}
	return 0;
}

