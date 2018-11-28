#include <iostream>
#include <conio.h>
using namespace std;
int cerca_sink(int,int);
int H,W,quota[102][102],assegnata[102][102],assegnate,j,i;
int direzione(int,int);
char mappa[102][102],nuovamappa[102][102],ch;



int main (void)
	{

	int T,k,count_sink, area,riga,colonna,contatore,x,y;

//	for (i=0;i<=256;i++)
//		{ch=i;cout << "i=" << i << "ch= " <<ch << "\n";}
		
	cin >> T;
	for (i=1;i<=T;i++)
		
		{
	for (j=0;j<=101;j++)
		for (k=0;k<=101;k++){
			quota[j][k] = 0;
			mappa[j][k]= 42;
			nuovamappa[j][k]= 42;
			assegnata[j][k]=0;
			}
		count_sink=0;
		assegnate=0;
		cin >> H;
		cin >> W;
		area=H*W;
		for(j=1;j<=H;j++)
			for(k=1;k<=W;k++)
				cin >> quota[j][k];
//contorno
		for(j=0;j<=W+1;j++)
			quota[0][j]=15000;
		for(j=0;j<=W+1;j++)
			quota[H+1][j]=15000;
		for(j=0;j<=H+1;j++)
			quota[j][0]=15000;
		for(j=0;j<=H+1;j++)
			quota[j][W+1]=15000;


//identifica i sink e dagli una lettera provvisoria
for (j=1;j<=H;j++){
	for (k=1;k<=W;k++)
		if(cerca_sink(j,k)==1){
			count_sink++;
			mappa[j][k]=count_sink+64;
			assegnata[j][k]=1;
			assegnate++;
//			cout << "* "; 
			} 
//		else
//			cout << quota [j][k] << " ";
//cout << "\n";
}
//cout << "\n";
//
//for (j=1;j<=H;j++){
//	for (k=1;k<=W;k++)
//		cout << quota[j][k];
//cout << "\n";
//}

//	cout << "\n";
//	for (j=1;j<=H;j++){
//	for (k=1;k<=W;k++)
//		cout << mappa[j][k];
//cout << "\n";
//}
//for (j=1;j<=H;j++){
//	for (k=1;k<=W;k++)
//		cout << direzione(j,k);
//cout << "\n";
//	}

//for (j=1;j<=H;j++){
//	for (k=1;k<=W;k++)
//		cout << assegnata[j][k];
//cout << "\n";
//	}

ricircolo:
	for (j=1;j<=H;j++){
		for (k=1;k<=W;k++)
			if(assegnata[j][k]==0) {
				switch(direzione(j,k)){
					case 0:
						riga=j;
						colonna=k;
						break;
					case 1:
						riga=j-1;
						colonna=k;
						break;
					case 2:
						riga=j;
						colonna=k-1;
						break;
					case 3:
						riga=j;
						colonna=k+1;
						break;
					case 4:
						riga=j+1;
						colonna=k;
						break;
					}
				if(assegnata[riga][colonna]==1) {
					assegnata[j][k]=1;
					mappa[j][k]=mappa[riga][colonna];
					assegnate++;
					}
				}
		}
	if(assegnate<area)goto ricircolo;




//riordina lettere
	contatore=0;
	nuovamappa[1][1]=97;
	for (j=1;j<=H;j++)
		for (k=1;k<=W;k++)
			if(mappa[j][k]==mappa[1][1])
				nuovamappa[j][k]=nuovamappa[1][1];

	for (j=1;j<=H;j++)
		for (k=1;k<=W;k++)
			if(nuovamappa[j][k]==42){
				contatore++;
				nuovamappa[j][k]=97+contatore;
				for(x=1;x<=H;x++)
					for(y=1;y<=W;y++){
						if((mappa[x][y]==mappa[j][k])&&(nuovamappa[x][y]==42))
							nuovamappa[x][y]=nuovamappa[j][k];
						}
				}



	//cout << "Case #" << i << ":\n";
	//for (j=1;j<=H;j++){
	//for (k=1;k<=W;k++)
	//	cout << quota[j][k];
	//cout << "\n";}

	//cout << "Case #" << i << ":\n";
	//for (j=1;j<=H;j++){
	//for (k=1;k<=W;k++)
	//	cout << mappa[j][k];
	//cout << "\n";}

	cout << "Case #" << i << ":\n";
	for (j=1;j<=H;j++){
	for (k=1;k<=W;k++)
		cout << nuovamappa[j][k]<< " ";
	cout << "\n";}







//		getch();
}
}
int cerca_sink(int x,int y)
	{
	if((quota[x][y]<=quota[x-1][y])
	&&(quota[x][y]<=quota[x+1][y])
	&&(quota[x][y]<=quota[x][y-1])
	&&(quota[x][y]<=quota[x][y+1]))
		return (1);
	else return (0);
	}

int direzione(int x, int y)
	{
	int dir,basso;
	dir=0;
	basso=quota[x][y];
	if(quota[x-1][y]<basso){
		basso=quota[x-1][y];
		dir=1;}
	if(quota[x][y-1]<basso){
		basso=quota[x][y-1];
		dir=2;}
	if(quota[x][y+1]<basso){
		basso=quota[x][y+1];
		dir=3;}
	if(quota[x+1][y]<basso){
		basso=quota[x+1][y];
		dir=4;}
	return(dir);
	}
	
