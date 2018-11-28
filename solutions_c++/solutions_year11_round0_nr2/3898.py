#include <iostream>
#include <vector>
#include <list>
#include <string>


using namespace std;


void reportarV(const vector< char >& v)
{
    vector< char > v2(v);
    int i=0;

    for(i=0;i<v.size();i++)
        cout<<v2[i]<<" ";
    cout<<endl;
}

void reportarV(const vector< string >& v)
{
    vector< string > v2(v);
    int i=0;

    for(i=0;i<v.size();i++)
        cout<<v2[i]<<" ";
    cout<<endl;
}

void reportarString(string cad)
{
    int i=0;

    cout<<"[";
    for(i=0;i<cad.size();i++)
    {
        if(i==cad.size()-1)
            cout<<cad[i];
        else
            cout<<cad[i]<<", ";
    }
    cout<<"]";
}

vector<string> v_comb, v_op;
vector<char> v_car;

string applyComb(string cad, string comb_t)
{
    string subcad1=cad.substr(cad.size()-2);
    string comb1=comb_t.substr(0,1)+comb_t.substr(1,1);
    string comb2=comb_t.substr(1,1)+comb_t.substr(0,1);
    string cadS=cad;

    if(subcad1.compare(comb1)==0 || subcad1.compare(comb2)==0)
        cadS=cad.substr(0,cad.size()-2)+comb_t.substr(2,3);

    return cadS;
}

string verificarCombs(string cad, vector<string> v_comb)
{
    int i=0;

    for(i=0;i<v_comb.size();i++)
        cad=applyComb(cad,v_comb[i]);
    return cad;
}

string applyOp(string cad, string op_t)
{
    string op1=op_t.substr(0,1);
    string op2=op_t.substr(1,1);
    string cadS=cad;

    int b1=cad.find(op1);
    int b2=cad.find(op2);

    if(b1!=-1 && b2!=-1)
        cadS="";

    return cadS;
}

string verificarOps(string cad, vector<string> v_op)
{
    int i=0;

    for(i=0;i<v_op.size();i++)
        cad=applyOp(cad,v_op[i]);
    return cad;
}

string resolver()
{
    int i=0;
    string cad;
    cad+=v_car[0];
    for(i=1;i<v_car.size();i++)
    {
        cad+=v_car[i];
        if(cad.size()>=2)
        {
            cad=verificarCombs(cad,v_comb);
            cad=verificarOps(cad,v_op);
        }
    }
    return cad;
}

int main()
{
    int nc,i=0,j=0,n,n_comb,n_op,n_car;
    string comb,op,resp;
    char car;

    cin>>nc;
    for(i=0;i<nc;i++)
    {
        v_comb.clear();
        v_op.clear();
        v_car.clear();
        cin>>n_comb;
        for(j=0;j<n_comb;j++)
        {
            cin>>comb;
            v_comb.push_back(comb);
        }
        cin>>n_op;
        for(j=0;j<n_op;j++)
        {
            cin>>op;
            v_op.push_back(op);
        }
        cin>>n_car;
        for(j=0;j<n_car;j++)
        {
            cin>>car;
            v_car.push_back(car);
        }
        resp=resolver();
        cout<<"Case #"<<(i+1)<<": ",
        reportarString(resp);
        cout<<endl;
    }
    return 0;
}
