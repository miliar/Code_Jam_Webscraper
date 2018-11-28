/*#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;


int main()
{
	//vector<int> a(5);
	//vector<vector<int> > prueba(8,a);
	/*vector<vector<int> > prueba;
	prueba.push_back(*(new vector<int>));
	prueba[0].push_back(9);
	cout<<prueba[0][0];

	vector<vector<int> > memo;
	vector<int> temp(150);
	memo=*(new vector<vector<int> >(150,temp));
	memo[0][0]=9;
	cout<<memo[0][0];

	return 0;
}*/

#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <queue>

using namespace std;

const int entrando=1;
const int saliendo=2;
const int A=4;
const int B=5;
struct time
{
	int hora;
	int minuto;
	time()
	{
	}
	time(int _hora,int _minuto)
	{
		hora=_hora;
		minuto=_minuto;
	}
};


struct evento
{
	int tipo;
	int estacion;
	time hora;
	evento(){}
	evento(int _tipo,int _estacion,time _hora)
	{
		tipo=_tipo;
		estacion=_estacion;
		hora=_hora;
	}
};

class sorting
{
public:
	bool operator ()(const evento& a,const evento& b)
	{
		
		if(a.hora.hora==b.hora.hora && a.hora.minuto==b.hora.minuto && a.tipo==b.tipo)
		{
			if(a.estacion>b.estacion)
			{
				return true;
			}
			return false;
		}
		if(a.hora.hora==b.hora.hora && a.hora.minuto==b.hora.minuto)
		{
			if(b.tipo==entrando)
			{
				return true;
			}
			return false;
		}
		else
		{
			if(a.hora.hora>b.hora.hora)
			{
				return true;
			}
			else if(a.hora.hora==b.hora.hora && a.hora.minuto>b.hora.minuto)
			{
				return true;
			}
		}

		return false;
	}
};



time sumarTiempo(time a,int turn)
{
	int temp=59-a.minuto;
	if(temp>=turn)
	{
		a.minuto+=turn;
	}
	else
	{
		turn-=temp;
		turn-=1;
		a.minuto=0;
		a.minuto+=turn;
		a.hora+=1;
	}
	return a;
}

int main()
{
	ifstream entrada("B-large.in");
	ofstream salida("salidaTrenes.out");
	int N;
	entrada>>N;
	for(int _N=0;_N<N;_N++)
	{
		int T,NA,NB;
		entrada>>T>>NA>>NB;
		priority_queue<evento,vector<evento>,sorting> eventos;
		for(int _NA=0;_NA<NA;_NA++)
		{
			int hora,minuto;
			char s;
			entrada>>hora>>s>>minuto;
			time t1(hora,minuto);
			evento e1(saliendo,A,t1);
			eventos.push(e1);
			entrada>>hora>>s>>minuto;
			time t2(hora,minuto);
			t2=sumarTiempo(t2,T);
			evento e2(entrando,B,t2);
			eventos.push(e2);
			
		}
		for(int _NB=0;_NB<NB;_NB++)
		{
			int hora,minuto;
			char s;
			entrada>>hora>>s>>minuto;
			time t1(hora,minuto);
			evento e1(saliendo,B,t1);
			eventos.push(e1);
			entrada>>hora>>s>>minuto;
			time t2(hora,minuto);
			t2=sumarTiempo(t2,T);
			evento e2(entrando,A,t2);
			eventos.push(e2);
		}

		int ta=0,tb=0,tea=0,teb=0;

		while(!eventos.empty())
		{
			evento temp=eventos.top();
			eventos.pop();
			if(temp.tipo == saliendo)
			{
				if(temp.estacion==A)
				{
					if(tea>0)
					{
						tea--;
					}
					else
					{
						ta++;
					}
				}
				if(temp.estacion==B)
				{
					if(teb>0)
					{
						teb--;
					}
					else
					{
						tb++;
					}
				}
			}
			else
			{
				if(temp.estacion==A)
				{
					tea++;
				}
				else
				{
					teb++;
				}
			}
		}
		salida<<"Case #"<<_N+1<<": "<<ta<<" "<<tb<<endl;
		
	}
	

/*	time t(3,59);
	t=sumarTiempo(t,1);
	cout<<t.hora<<":"<<t.minuto<<endl;*/

/*	evento e1(entrando,A,time(5,0));
	evento e2(saliendo,A,time(5,0));
	evento e3(entrando,B,time(5,0));
	evento e4(saliendo,B,time(5,0));
	evento e5(entrando,A,time(5,0));
	evento e6(saliendo,B,time(5,0));
	evento e7(entrando,A,time(5,0));
	evento e8(saliendo,B,time(5,0));
	evento e9(entrando,B,time(5,0));
	evento e10(saliendo,A,time(5,0));
	
	sorting p;
	//p.operator ()(e1,e2);
	priority_queue<evento,vector<evento>,sorting> eventos;
	eventos.push(e1);
	eventos.push(e2);
	eventos.push(e3);
	eventos.push(e4);
	eventos.push(e5);
	eventos.push(e6);
	eventos.push(e7);
	eventos.push(e8);
	eventos.push(e9);
	eventos.push(e10);
	while(!eventos.empty())
	{
		evento temp=eventos.top();
		eventos.pop();
	}*/
	return 0;
}