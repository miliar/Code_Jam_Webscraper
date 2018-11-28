#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <fstream>
#include <sstream>
#include<map>
using namespace std;
 
string convertInt(int number)
{
   stringstream ss;//create a stringstream
   ss << number;//add number to the stream
   return ss.str();//return a string with the contents of the stream
}
 
int convertString(string S)
{
        stringstream ss;
        ss << S;
        int m;
        ss>>m;
        return m;
}
 
map < string,vector<string>  > Set;
int main()
{
        //ifstream fin ("in.txt");
        //ofstream fout ("out.txt");
        int n;
        cin>>n;
        int C = 0;
        long long zzz=0; 
	vector<long> done;
        for (int i = 1; i <= n; i ++)
        {	zzz=0;
                int S1, S2;
                cin>>S1>>S2;
                for (int i = S1; i < S2; i++)
                {
                        string P1 = convertInt(i);
                        
                        for (int j = 0; j < P1.size(); j ++)
                        {
                                
                                string l,m;
                                l = m = "";
                                l = P1.substr(j, P1.size()-j+1);
                                if (j > 0)
                                        m = P1.substr(0, j);
                                string P2 = l + m ;
                                string A1, A2;
                                A1 = P1;
                                A2 = P2;
                                if (A2[0] == '0')continue;
                                if (A1 == A2) continue;
                                int X = convertString(A2);
                                if (X > S2 || X < S1)
                                        continue;
                                //pair <string, string> L = make_pair( (A1 > A2)? A2: A1, (A1 > A2)? A1: A2);
				string min=(A1 > A2)? A2: A1;
				string max=(A1 > A2)? A1: A2;
                                bool found = false;
				if(Set.find(min)!=Set.end())
                                for (int k = 0 ; k < Set[min].size() && !found; k ++)
                                {
                                        if (Set[min][k] == max)
                                                found = true;
                                }
                                if (!found)
                                        Set[min].push_back(max),zzz++;
                        }
                }
                cout<<"Case #"<<i<<": "<<zzz<<endl;
                Set.clear();
        }
        return 0;
}  
