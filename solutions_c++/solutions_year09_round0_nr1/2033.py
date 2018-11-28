#include<iostream>
#include<fstream>
#include<string>
#include<set>
#include<vector>
#include<algorithm>
using namespace std;

int main(){
    int l,d,n,k,cantsolution;
    set<string> s,aux1,aux2;
    vector<string> v;
    set<string>::iterator it;
    string str;
    ifstream f("A-large.in");
    string solutiontext;
    cin>>l>>d>>n;
    for(int i=0;i<d;i++){
        cin>>str;
        s.insert(str);
    }
    aux1=s;

    for(int i=0;i<n;i++){
        cin>>str;
        k=0;
        for(int j=0;j<str.size();j++){
            if(str[j]=='('){
                k=j;
                while(str[k]!=')')
                    k++;
                v.push_back(str.substr(j+1,k-j-1));
                j=k;
            }
            else
				{
					string apa(1,str[j]);
                v.push_back(apa);//vector de palabras
				}
        }
        for(int j=0;j<v.size();j++)
        {

            for(it=aux1.begin();it!=aux1.end();it++)
            {
                for(int m=0;m<v[j].size();m++)
                {
                if(v[j][m]==(*it)[j]){aux2.insert(*it);}
                }
            }
            swap(aux2,aux1);
            aux2.clear();//EN AUX1 me quedan todas las palabras posiblemente validas
        }
        cout<<"Case #"<<i+1<<": "<<aux1.size()<<endl;
            v.clear();
            aux1=s;
    }
    return 0;
}
