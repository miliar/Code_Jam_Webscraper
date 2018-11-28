#include <iostream>

using namespace std;

struct lista{
    int dato;
    lista *next;
};

lista *creaLista(int n)
{    
     lista *L=new lista;     
     lista *p=L;
     p->dato=0;
     for (int i=1; i<n; i++){
         p->next=new lista;
         p=p->next;
         p->dato=i;
     }
     p->next=L;
     return L;
}

int main()
{
    int casos;
    cin>>casos;
    for (int ccasos=1; ccasos<=casos; ccasos++)
    {
        int r,k,n;
        cin>>r>>k>>n;
        lista *L=creaLista(n);
        lista *aux=L;
        for(int i=0; i<n; i++)
        {
            cin>>aux->dato;
            aux=aux->next;
        }
        int corredores=0;
        aux=L;
        int total=0;
        int grupos=0;
        while(r>0)
        {
            if (corredores+aux->dato<=k && grupos<n){
                corredores+=aux->dato;
                total+=aux->dato;
                aux=aux->next;
                grupos++;
            }
            else{
                 r--;
                 corredores=0;
                 grupos=0;
            }
        }
        cout << "Case #"<<ccasos<<": "<<total<<endl;
    }
    return 0;
}
