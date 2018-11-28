#include <iostream>
#include <queue>
#include <string>
using namespace std;

#define DBG(x) cout<<#x<<" = "<<x<<"\n";

int main()
{
	int pocet,i,j,x,o,pocx,poco,poct;
	char m[4][4],hladany,pismeno;
	bool bodka,spravnost;
	cin>>pocet;

	
	for(int poc=0;poc<pocet;poc++){
		x=0;o=0;
		bodka=false;
		//nacitavanie
		for(i=0;i<4;i++){
			for(j=0;j<4;j++){
				cin>>m[j][i];
				if(m[j][i]=='.') bodka=true;
			}
		}
		//zvisly smer
		poct=0;pocx=0;poco=0;
		for(j=0;j<4;j++)
		{poct=0;pocx=0;poco=0;
		
		for(i=0;i<4;i++){
			pismeno=m[i][j];
			if(pismeno=='X') pocx++;
			else if(pismeno=='O') poco++;
			else if(pismeno=='T') poct++; 
		}
		if((pocx+poct)==4) x++;// vyhral x else
		if((poco+poct)==4) o++; //vyhral y 
		} 
		
		//vodorovny smer
		poct=0;pocx=0;poco=0;
		for(j=0;j<4;j++)
		{poct=0;pocx=0;poco=0;
		for(i=0;i<4;i++){
			pismeno=m[j][i];
			if(pismeno=='X') pocx++;
			else if(pismeno=='O') poco++;
			else if(pismeno=='T') poct++; 
		} if((pocx+poct)==4) x++;// vyhral x else
		if((poco+poct)==4) o++; //vyhral y 
		}
		
		/*for(i=0;i<4;i++){
			if(m[0][i]=='T') hladany=m[1][i];
			else hladany=m[0][i];
			spravnost=1;
			for(j=0;j<4;j++){
				if(m[j][i]==hladany) continue;
				else {spravnost=0; break;}
			}
			if(spravnost){
				//tak vyhral hladany
				if(hladany=='X') x++; else o++;
			}
		}*/
		//diagonaly
		poct=0;pocx=0;poco=0;
		for(i=0;i<4;i++){
			pismeno=m[i][i];
			if(pismeno=='X') pocx++;
			else if(pismeno=='O') poco++;
			else if(pismeno=='T') poct++;
		}
		if((pocx+poct)==4) x++;// vyhral x
		else if((poco+poct)==4) o++; //vyhral y
		
		poct=0;pocx=0;poco=0; 
		for(i=0;i<4;i++){     
			pismeno=m[i][3-i];
			if(pismeno=='X') pocx++;     
			else if(pismeno=='O') poco++;     
			else if(pismeno=='T') poct++; 
		} 
		if((pocx+poct)==4) x++;// vyhral x else
		if((poco+poct)==4) o++; //vyhral y 
		cout<<"Case #"<<poc+1<<": ";
		if(x) cout<<"X won"; 
		else if(o) cout<<"O won"; 
		else if(!bodka) cout<<"Draw"; 
		else cout<<"Game has not completed"; 
		cout<<"\n";
		
	}
}
