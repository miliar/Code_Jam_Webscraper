#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <queue> 
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <utility> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <cctype> 
#include <string> 
#include <cstring> 
#include <ctime> 

using namespace std;

char in_file[] = "B-small-attempt1.in";
char out_file[] = "B-small-out.data";


map<int,vector<vector<int> > > mapper;

void gen_all_nums()
{
    int i,j,k;
    int sum;
    vector<int> tmp;
    vector<int>::iterator tmp_end;
    for (i=0; i<=10; i++)
    {
        for (j=0; j<=10; j++)
        {
            for (k=0; k<=10; k++)
            {
                tmp.clear();
                tmp.push_back(i);
                tmp.push_back(j);
                tmp.push_back(k);
                sort(tmp.begin(), tmp.end());
                sum = i + j + k;
                mapper[sum].push_back(tmp);
            }
        }
    }

    map<int, vector<vector<int> > >::iterator iter;
    vector<vector<int> >::iterator end;
    for (iter=mapper.begin(); iter!=mapper.end();iter++)
    {
        sort((iter->second).begin(), (iter->second).end());
        end = unique((iter->second).begin(), (iter->second).end());
        (iter->second).erase(end, (iter->second).end());
    }
}

void get_all_z(int persons, vector<int> &scores, vector<vector<vector<int> > > &vec)
{
    int i,j,k,m,n;
    int cur;

    vector<int> indexer(persons, 0);
    vector<vector<int> > temp;
    i = 0;
    j = 0;

    while(i>=0)
    {
        while(i<persons && indexer[i]<mapper[scores[i]].size())
        {
            temp.push_back(mapper[scores[i]][indexer[i]]);
            indexer[i]++;
            i++;
        }
        
        if (i == persons)
        {
            vec.push_back(temp);
            i--;
        }
        
        if (indexer[i] == mapper[scores[i]].size())
        {
            indexer[i] = 0;
            i--;
        }

        if (i<0)
            break;
        else
            temp.erase(temp.begin()+i, temp.end());
    }
}

int deal_all_z(vector<vector<vector<int> > > &vec, int surp_nuber, int lower_score)
{
    int i,j,k,t;
    int num;
    int apart_count;
    int more_count;
    int surp_count = 0;
    int max_person;
    int max_ret = 0;
    bool error = false;

    for (i=0; i<vec.size(); i++)
    {
        surp_count = 0;
        max_person = 0;
        error = false;

        for (j=0; j<vec[i].size(); j++)
        {
            if (vec[i][j][0]+2 == vec[i][j][2])
            {
                surp_count++;
            }
            else if (vec[i][j][0]+2 < vec[i][j][2])
            {
                error=true;
                break;
            }

            more_count = 0;
            for (k=0; k<3; k++)
            {
                if (vec[i][j][k] >= lower_score)
                    more_count++;
            }

            if (more_count > 0)
            {
                max_person++;
            }
        }

        if (!error && surp_count == surp_nuber)
        {
            max_ret = (max_person > max_ret) ? max_person : max_ret;
        }
    }

    return max_ret;
}

int main()
{
    int case_count;
    int i,j,t;
    string line;
    int len;
    int persons,surp_nuber,lower_score;
    vector<int> scores;
    int sco;
    int ret;
    vector<vector<vector<int> > > test;

    gen_all_nums();

    freopen(in_file, "r", stdin);
    freopen(out_file,"w", stdout);

    cin >> case_count;
    cin.get();
    
    for (t=1;t<=case_count;t++)
    {
        scores.clear();
        cin >> persons >> surp_nuber >> lower_score;
        for (i=0; i<persons; i++)
        {
            cin >> sco;
            scores.push_back(sco);
        }

        test.clear();
        get_all_z(persons, scores, test);
        ret = deal_all_z(test, surp_nuber, lower_score);

        cout << "Case #" << t << ": " << ret << endl;
    }

	return 0;    
}
