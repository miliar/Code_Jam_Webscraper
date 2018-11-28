#include<iostream>
#include<fstream>
#include<map>
#include<string>
#include<set>
using namespace std;

map<char,set<char>> opp_map;
map<string,string> com_map;

int n;
long main()
{
   
    ifstream fin("input.in");
    ofstream fout("output.out");

    fin>>n;
    for(int ca = 1;ca<=n;++ca)
    {
        opp_map.clear();
        com_map.clear();
        string target;
        string result;
        int c_num;
        int d_num;
        int len;
        fin>>c_num;
        string temp;
        for(int i = 0;i!=c_num;++i)
        {
            fin>>temp;
            string s1 = temp.substr(0,2);
            string s2 = temp.substr(2,1);
			com_map[s1]=s2.substr(0,1);
            s1.append(s1.substr(0,1));
			com_map[s1.substr(1,2)]=s2.substr(0,1);
        }
        fin>>d_num;
        for(int i = 0;i!=d_num;++i)
        {
            fin>>temp;
			opp_map[temp[0]].insert(temp[1]);
			opp_map[temp[1]].insert(temp[0]);
        }

        fin>>len;

        fin>>target;
        //here to erase
		set<char>::iterator iter;
        for(string::size_type i = 0 ;i<target.size();)
        {
            if(com_map.count(target.substr(i,2))>0)
            {
                
                result.append(com_map[target.substr(i,2)]);
				i+=2;
                continue;
            }
            else
            {
                if(opp_map.count(target[i])>0)
                {   
					string::size_type last = 6000;
					
					for(iter = opp_map[target[i]].begin();
						iter != (opp_map[target[i]]).end();
						++iter)
					{
						char cc = *iter;
						for(string::size_type j = i+1;j<target.size();++j)
						{
							if(target[j]==cc && com_map.count(target.substr(j-1,2)) == 0)
							{
								if(j<last) last = j;
							}
						}
					}
					if(last != 6000)
					{
						i = last +1;
                        result.clear();
					}
					else
					{
						result.append(target.substr(i,1));
						++i;
					}
                }
				else
				{
					result.append(target.substr(i,1));
					++i;
				}
                
            }

        }
		fout<<"Case #"<<ca<<": [";
		bool haveOut = false;
		for(string::size_type i = 0;i!=result.size();++i)
		{
			if(haveOut) fout<<", ";
			fout<<result[i];
            haveOut = true;
		}
		fout<<"]"<<endl;
    }
    fin.close();
    fout.close();
}