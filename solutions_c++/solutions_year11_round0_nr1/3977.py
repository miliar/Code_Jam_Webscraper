#include <iostream>
#include <list>

using namespace std;

int main()
{
	int casos, res, contador, botones, i, num;
	int sgteNaranjo, sgteAzul, estadoNaranjo, estadoAzul;
	bool pushNaranjo, pushAzul;
	char color;
	string s;
	string accionAzul, accionNaranjo;
	list<int> naranjo, azul;
	list<char> ordenColor;
	list<int> ordenNumero;
	cin >> casos;
	
	contador = 1;
	
	while(contador <= casos)
	{
		res = 0;
		naranjo.clear();
		azul.clear();
		ordenColor.clear();
		ordenNumero.clear();
		estadoNaranjo = 1;
		estadoAzul = 1;
		
		cin >> botones;
		
		for(i = 0; i < botones; i++)
		{
			cin >> color;
			cin >> num;
			
			ordenColor.push_back(color);
			ordenNumero.push_back(num);
			
			if(color == 'O')
				naranjo.push_back(num);
			else
				azul.push_back(num);
		}
		
		//Seccion de simulacion
		
		while(!ordenColor.empty())
		{
			pushNaranjo = false;
			pushAzul = false;
			
			sgteNaranjo = naranjo.front();
			sgteAzul = azul.front();
			
			int DNaranjo = sgteNaranjo - estadoNaranjo;
			int DAzul = sgteAzul - estadoAzul;
			
			if(DNaranjo > 0)
			{
				estadoNaranjo++;
				accionNaranjo = "Move to ";
			}
			else if(DNaranjo < 0)
			{
				estadoNaranjo--;
				accionNaranjo = "Move to ";
			}
			else if(ordenColor.front() == 'O' && !pushAzul)
			{
				ordenColor.pop_front();
				ordenNumero.pop_front();
				naranjo.pop_front();
				accionNaranjo = "Push button ";
				pushNaranjo = true;
			}
			else
				accionNaranjo = "Stay at button ";
			
			if(DAzul > 0)
			{
				estadoAzul++;
				accionAzul = "Move to ";
			}
			else if(DAzul < 0)
			{
				estadoAzul--;
				accionAzul = "Move to ";
			}
			else if(ordenColor.front() == 'B' && !pushNaranjo)
			{
				ordenColor.pop_front();
				ordenNumero.pop_front();
				azul.pop_front();
				accionAzul = "Push button ";
				pushAzul = true;
			}
			else
				accionAzul = "Stay at button ";
			
			//cout << accionNaranjo << " " << estadoNaranjo << " " << accionAzul << " " << estadoAzul << endl;
			
			
			res++;
		}
		
		
		//Fin seccion
		
		
		cout << "Case #" << contador << ": " << res << endl;
		contador++;
	}
	
	return 0;
}
