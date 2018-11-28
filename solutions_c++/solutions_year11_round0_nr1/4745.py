// A_BotTrust.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "iostream"
using namespace std;
struct rA
{
	int boton;
	char robot;
};

void Accion(int &posrob,const int posboton,int &time, const int ProxBotDelOtroRobot, int &PosDelOtroRobot)
{
	while(posrob != posboton)
	{
		if(posrob<posboton)
		{
			posrob++;
			time++;
		}
		else
		{
			posrob--;
			time++;
		}
		if(PosDelOtroRobot < ProxBotDelOtroRobot)
		{
			PosDelOtroRobot++;
		}
		if(PosDelOtroRobot>ProxBotDelOtroRobot)
		{
			PosDelOtroRobot--;
		}
	}
	time++;
	if(PosDelOtroRobot < ProxBotDelOtroRobot)
	{
		PosDelOtroRobot++;
	}
	if(PosDelOtroRobot>ProxBotDelOtroRobot)
	{
		PosDelOtroRobot--;
	}

}

int main(int argc, char* argv[])
{
	int orange[101],blue[101],N,contO,contB,T,posO,posB,time, cont2,poscarg,poscargO,poscargB;
	char color[101],ProxBotonB,ProxBotonO;
	rA rAux,rEve;

	freopen("l.in","rt+",stdin);
	freopen("large.out","w+",stdout);
	scanf("%d",&N);
	
	for(int cont=0;cont<N;cont++)
	{
		scanf("%d",&T);
		poscargO=poscargB=0;
		for(cont2=0;cont2<T;cont2++)
		{
			cin >> rAux.robot;
			
			scanf("%d",&rAux.boton);
			if(rAux.robot=='O')
			{
				orange[poscargO]=rAux.boton;
				poscargO++;
			}
			else
			{
				blue[poscargB]=rAux.boton;
				poscargB++;
			}
			color[cont2]=rAux.robot;
		}
		poscarg=cont2;
		cont2=0;
		time=contO=contB=0;
		posB=posO=1;
		while(cont2<poscarg)
		{
			rEve.robot=color[cont2];		
			if(rEve.robot=='O')
			{
				rEve.boton=orange[contO];
			}
			else
			{
				rEve.boton=blue[contB];
			}
			ProxBotonO=orange[contO];
			ProxBotonB=blue[contB];
			if(rEve.robot=='B')
			{
				Accion(posB,rEve.boton,time,ProxBotonO,posO);
				contB++;
			}
			else
			{
				Accion(posO,rEve.boton,time,ProxBotonB,posB);
				contO++;
			}
			cont2++;
			
		}
		printf("Case #%d: %d\n",cont+1,time);

	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}

