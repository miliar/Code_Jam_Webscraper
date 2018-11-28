#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int abs(int x)
{
  return (x>0?x:-x);
}

int main()
{
    int t;
    cin>>t;
    int n;
    for(int i=1; i<=t; i++)
    {
        cin>>n;
        vector <int> pos;
	vector <char> turno;
        for(int ii=0; ii<n; ii++)
	{
            char c; 
	    int val;
	    cin>>c>>val;
            pos.push_back(val);
	    turno.push_back(c);
        }
        
        int resp,posO,posB,aux;
        char toca='A';
        
	resp=aux=0;
	posO=posB=1;
	
        for(int j=0; j<pos.size(); j++)
	{
            if(turno[j]=='O')
	    {
                if(turno[j]==toca)
		{
                    resp+=abs(pos[j]-posO)+1;
                    aux += abs(pos[j]-posO)+1;
                    toca = turno[j];
                    posO = pos[j];
                    continue;
                }
                
                int dif = abs(pos[j]-posO);
		
                if(dif-aux<=0) dif=0;
                else dif-=aux;
		
                resp+= dif+1;
                aux=dif+1;
                posO = pos[j];
                toca = turno[j];
            }
            else
	    {
                if(turno[j]==toca)
		{
                    resp+=abs(pos[j]-posB)+1;
                    aux+=abs(pos[j]-posB)+1;
                    toca=turno[j];
		    posB = pos[j];
                    continue;
                }
                int dif=abs(pos[j]-posB);
                
		if(dif-aux<=0) dif=0;
                else dif-=aux;
		
                resp+=dif+1; 
		aux=dif+1;
		posB=pos[j];
		toca=turno[j];
            }
        }
        cout<<"Case #"<<i<<": "<<resp<<endl;
        
    }
    return 0;
}