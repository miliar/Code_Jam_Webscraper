#include<iostream>
#include<string>
#include<sstream>
#include<fstream>
#include<vector>
#include<algorithm>

using namespace std;



int ropeintranet(int i, vector<vector<int> > aarrays, vector<vector<int> > barrays)
{
    vector<int> a = aarrays[i];
    vector<int> b = barrays[i];
    int n = aarrays[i].size();
    int res = 0;

    //cout << "n:" << n << endl;
    
    
    for(int i=0; i < n; i++)
        for(int j=i+1; j < n; j++)
        {
            //cout << "a:" << a[i] << " " << a[j] << endl;
            //cout << "b:" << b[i] << " " << b[j] << endl;
            
            if(a[i] - a[j] > 0 && b[i] - b[j] < 0)
                res++;
            else if(a[i] - a[j] < 0 && b[i] - b[j] > 0)
                res++;
        }
    //cout << "res=" << res << endl;
    return res;
}

int main(int argc, char** argv)
{
    ifstream ifs(argv[1]);
    string buf;
    int line = 1;
    int n_get = 0;

    int tcase;
    vector <int> narray;
    vector<vector<int> > aarrays;
    vector<vector<int> > barrays;
    vector<int> tmp_a, tmp_b;
    
    while(ifs && getline(ifs, buf)){
        istringstream iss(buf);
        
        int n,a,b;

        if(line == 1)
            iss >> tcase;
        else if(n_get == 0)
        {
            iss >> n;
            n_get = n;
            //cout << "n:" << n << endl;
        }
        else if(n_get > 0)
        {
            iss >> a >> b;
            //cout << " " << a << " " << b;
            tmp_a.push_back(a);
            tmp_b.push_back(b);
            n_get --;
            if(n_get == 0)
            {
                aarrays.push_back(tmp_a);
                barrays.push_back(tmp_b);
                tmp_a.clear(); tmp_b.clear();
            }
        }
        line++;
    }

    {
        ofstream ofs("result.txt");
        for(int i=0; i<tcase; i++){
            int res = ropeintranet(i, aarrays, barrays);
            cout << "Case #" << i+1 << ": " << res << endl;
            ofs << "Case #" << i+1 << ": " << res << "\r\n";
        }
    }


    return 0;
}