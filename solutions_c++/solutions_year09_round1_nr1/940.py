#include <iostream>
#include <vector>
#include <string>

using namespace std;

class solver{
public:
    vector<int> bases;
    void insertbase(int x);
    void showbases();
    int solve();
    bool happy(int i,int j);
};

bool solver::happy(int base,int val)
{
    vector<int> value;
    for(int i=0;i<100;i++)
    {
        int dividva=base;
        bool stayinlooper=true;
        for (int exp=1;val!=0;exp++) {
            value.push_back(val%base);
            val=val/base;
        }
        int sumadd=0;
        for(int i=0;i<value.size();i++)
        {
            sumadd=sumadd+value[i]*value[i];
        }
        vector<int> empty;
        value=empty;
        if (sumadd==1) {
            return true;
        }
        val=sumadd;
    }
    return false;
}

void solver::showbases(){
for(int x=0;x<bases.size();x++)
{
    cout <<bases[x] <<endl;
}
}

void solver::insertbase(int x){
    bases.push_back(x);
}

int solver::solve()
{
    int value=0;
    bool stayinloop=true;
    for(int j=2;stayinloop;j++)
    {
        for(int i=0;i<bases.size();i++)
        {
            if(!happy(bases[i],j)) break;
            if(i==bases.size()-1) stayinloop=false;
        }
        if(stayinloop==false) value= j;
    }
    return value;
}


int main()
{
    int numtestcases;
    cin >>numtestcases;
    cin.ignore();
    for(int i=1;i<=numtestcases;i++)
    {
        cout <<"Case #" <<i <<": ";
        int value=1;
        solver caser;

        // happy implementation here
        string tempstring;
        
        getline(cin,tempstring);
        bool stayinloop=true;
            for(int g=0;g<tempstring.size();g++)
            {

                if(tempstring.at(g)!=' ')
                {
                    if(tempstring.at(g)!='1'){
                        caser.insertbase(tempstring.at(g)-48);
                    }
                    else
                    {
                        if(g==(tempstring.size()-1))
                        {
                            caser.insertbase(tempstring.at(g)-48);
                        }
                        else if(tempstring.at(g+1)!=' ')
                        {
                            caser.insertbase(10);
                            g++;
                        }
                        else
                        {
                            caser.insertbase(1);
                        }
                    }
                }
            }
        //caser.bases.pop_back();
        value=caser.solve();

        //happy implementation ends here
        cout <<value <<endl;
    }
    return 0;
}


