#include <iostream>
#include <queue>

using namespace std;

void reportarCola(const queue<int>& cola)
{
    queue<int> cola2(cola);

    while(!cola2.empty())
    {
        cout<<cola2.front()<<" ";
        cola2.pop();
    }
}

int resolver(int nV,int nA,const queue<int>& colae)
{
    int s=0,st=0,i=0,c=0;
    queue<int> cola(colae);

    for(i=0;i<nV;i++)
    {
        s=0;
        c=0;
        while(s<=nA)//cada viaje
        {
            if(c==colae.size())
            {
                s=s+cola.front();
                break;
            }
            s=s+cola.front();
            if(s<=nA)
            {
                cola.push(cola.front());
                cola.pop();
            }
            c++;
        }
        s=s-cola.front();
        st=st+s;
    }
    return st;
}

int main()
{
    int nc,i=0,j=0;
    int r,k,n;
    int g,resp;

    cin>>nc;
    //cout<<endl<<"nc: "<<nc<<endl;
    for(i=0;i<nc;i++)
    {
        cin>>r>>k>>n;
        queue<int> cola;
        for(j=0;j<n;j++)
        {
            cin>>g;
            cola.push(g);
        }

        /*cout<<endl<<"r: "<<r<<endl;
        cout<<"k: "<<k<<endl;
        cout<<"n: "<<n<<endl;
        reportarCola(cola);*/

        resp=resolver(r,k,cola);
        cout<<"Case #"<<(i+1)<<": "<<resp<<endl;
        //cout<<"salida: "<<resp<<endl;
    }
    return 0;
}
