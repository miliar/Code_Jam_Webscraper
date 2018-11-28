#include <fstream>
#include <iostream>
#include <map>
#include <string>
#include <iomanip>

using namespace std;

//typedef map<string,bool,less<string>> map_; 

int main()
{
    int i_test,n_test;
    int S,Q,i,j,k,t;
    char *str_ = new char[150];
    string str;
    map <string,bool> eng;
    map <string,bool>::iterator i_eng;
    ifstream fin("a.in",std::ios::in);
    ofstream fout("a.out");
    fin >> n_test;
//    fscanf(fin,"%d",&n_test);
    for(i_test=0;i_test<n_test;i_test++)
    {
        fin >> S;
//        fscanf(fin,"%d",&S);
        cout << S << endl;
        fin.getline(str_,100);
        for(i=0;i<S;i++)
        {
            fin.getline(str_,100);
            cout << str_ << endl;
            str.assign(str_);
//              fin >> str;
//            fscanf(fin,"%s",&str);
            cout << str << endl;
//            cin >> j;
            eng[str]=false;
        }
//        printf("YES");
        for(i_eng=eng.begin();i_eng!=eng.end();i_eng++)
        {
            (*i_eng).second=false;
        }
        fin >> Q;
//        fscanf(fin,"%d",&Q);
        fin.getline(str_,100);
        k=0;
        t=0;
        for(i=0;i<Q;i++)
        {
            
            fin.getline(str_,100);
            cout << str_ << endl;
            str.assign(str_);
//            fscanf(fin,"%s",&str);
            if(!eng[str])
            {
                eng[str]=true;
                k++;
            }
            if(k==S)
            {
                for(i_eng=eng.begin();i_eng!=eng.end();i_eng++)
                {
                    (*i_eng).second=false;
                }
                eng[str]=true;
                k=1;
                t++;
                
            }
        }
        fout << "Case #" << i_test+1 <<": " << t << endl;
//        fprintf(fout,"Case #%d: %d",i_test+1,t);
    }
    cin >> i;
//    scanf("%d",&i);
    return 0;
}
