#include<iostream>

using namespace std;

int alt[100][100],dra[100][100];
void color(int i , int j ,int m , int n )
{
		int minalt,mini,minj,ni,nj,si,sj,wi,wj,ei,ej;		
		minalt= alt[i][j];
		ni = i-1; 
		nj = j;
//cout<<"21"<<endl;
		if((ni >= 0) && (alt[ni][nj] < alt[i][j]) && (minalt > alt[ni][nj]) ) { minalt = alt[ni][nj]; mini = ni ; minj= nj;} 
		wi = i;
		wj = j-1;
		if((wj >= 0) && (alt[wi][wj] < alt[i][j]) && (minalt > alt[wi][wj]) ) { minalt = alt[wi][wj]; mini = wi ; minj= wj;}
		ei = i;
		ej = j+1;
		if((ej < n) && (alt[ei][ej] < alt[i][j]) && (minalt > alt[ei][ej]) ) { minalt = alt[ei][ej]; mini = ei ; minj= ej;}
		si = i+1; 
		sj = j;
		if((si < m) && (alt[si][sj] < alt[i][j]) && (minalt > alt[si][sj]) ) { minalt = alt[si][sj]; mini = si ; minj= sj;}
		
//cout<<"22";
if( dra[mini][minj] < 65 )
{
	
	color(mini,minj,m,n);
}
//cout<<"23";

dra[i][j]= dra[mini][minj]; 

}

int main()
{
int i,j,counter,ctr,ni,nj,si,sj,ei,ej,wi,wj,m,n,ctr1,map[26],k,num;

cin>>num;
for (k=0;k<num;k++)
{
cin>>m>>n ; // m is the number of rows
counter=0;
for (i=0;i<26;i++)
	map[i]=-1;
for (i=0;i<m;i++)
	for(j =0; j<n;j++)
		{ cin>>alt[i][j]; dra[i][j] = 48;}
//cout<<"1"<<endl;
for (i=0;i<m;i++)
	for(j=0;j<n;j++)
		{
		ctr = 0;
		ni = i-1; 
		nj = j;
		if((ni >= 0) && (alt[ni][nj] < alt[i][j]) ) ctr =1;
//		if(ctr == 1)
//			cout<<i<<j<<"11";
		wi = i;
		wj = j-1;
		if((wj >= 0) && (alt[wi][wj] < alt[i][j]) ) ctr =1;
//		if(ctr == 1)
//			cout<<i<<j<<"12";		
		si = i+1; 
		sj = j;
		if((si < m) && (alt[si][sj] < alt[i][j]) ) ctr =1;
//if(ctr == 1)
//			cout<<i<<j<<"13";
		ei = i;
		ej = j+1;
		if((ej < n) && (alt[ei][ej] < alt[i][j]) ) ctr =1;
//if(ctr == 1)
//			cout<<i<<j<<"14"<<endl;
		if (ctr == 0)
		{
			dra[i][j] = 65+counter;
			
			counter++;
			//cout<<i<<j;
			//cout<<char(dra[i][j])<<" ";
		}
				
		}

//cout<<"2"<<counter<<endl;
if (counter == 0)
	{ dra[0][0]=65; counter++;}
for(i=0;i<m;i++)
	for(j=0;j<n;j++)
		{
//		cout<<i<<j<<endl;
		if(dra[i][j] < 65 )
			color(i,j,m,n);
		}
//cout<<"3";

ctr1=0;
for(i=0;i<m;i++)
	for(j=0;j<n;j++)
		{ 
		if(ctr1 == counter) 
			break;
		if(map[dra[i][j]-65] == -1)
  			map[dra[i][j]-65] = 97+ctr1++;
		}
cout<<"Case #"<<k+1<<":"<<endl;
//for(i=0;i<m;i++)
	//{
	//for(j=0;j<n;j++)
	//	cout<<char(dra[i][j])<<" ";
	//cout<<endl;	
	//}
for(i=0;i<m;i++)
	{
	for(j=0;j<n;j++)
		cout<<char(map[dra[i][j]-65])<<" ";
	cout<<endl;	
	}
}
return(0);
}


