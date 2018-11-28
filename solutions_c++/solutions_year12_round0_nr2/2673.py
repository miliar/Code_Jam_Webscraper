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

char in_file[] = "B-small-attempt0.in";
char out_file[] = "B-small-out.data";

map<int,vector<vector<int> > > mapper;

void gen_all_nums()
{
    int sum,avg,yu;
    vector<int> tmp;

    tmp.push_back(0);
    tmp.push_back(0);
    tmp.push_back(0);
    mapper[0].push_back(tmp);

    tmp.clear();
    tmp.push_back(0);
    tmp.push_back(0);
    tmp.push_back(1);
    mapper[1].push_back(tmp);

    for (sum=2; sum<=30; sum++)
    {
        avg = sum/3;
        yu  = sum%3;

        if (yu == 1)
        {
            tmp.clear();
            tmp.push_back(avg);
            tmp.push_back(avg);
            tmp.push_back(avg+1);
            mapper[sum].push_back(tmp);

            tmp.clear();
            tmp.push_back(avg-1);
            tmp.push_back(avg+1);
            tmp.push_back(avg+1);
            mapper[sum].push_back(tmp);
        }
        else if (yu == 2)
        {
            tmp.clear();
            tmp.push_back(avg);
            tmp.push_back(avg+1);
            tmp.push_back(avg+1);
            mapper[sum].push_back(tmp);

            tmp.clear();
            tmp.push_back(avg);
            tmp.push_back(avg);
            tmp.push_back(avg+2);
            mapper[sum].push_back(tmp);
        }
        else if (yu == 0)
        {
            tmp.clear();
            tmp.push_back(avg);
            tmp.push_back(avg);
            tmp.push_back(avg);
            mapper[sum].push_back(tmp);

            tmp.clear();
            tmp.push_back(avg-1);
            tmp.push_back(avg);
            tmp.push_back(avg+1);
            mapper[sum].push_back(tmp);        }
    }
}

int deal(vector<vector<int> > &vec, int surp_nuber, int lower_score)
{
    int i,j,k;
    int more_count;
    int surp_count = 0;
    int max_person = 0;

    for (i=0; i<vec.size(); i++)
    {
        if (vec[i][0]+2 == vec[i][2])
        {
            surp_count++;
        }

        more_count = 0;
        for (k=0; k<3; k++)
        {
            if (vec[i][k] >= lower_score)
                more_count++;
        }

        if (more_count > 0)
        {
            max_person++;
        }
    }

    if (surp_count == surp_nuber)
    {
        return max_person;
    }
    else
        return 0;
}

int get_all_z(int persons, vector<int> &scores, int surp_nuber, int lower_score)
{
    int i = 0;
    int cur_ret;
    int max_ret = 0;
    vector<int> indexer(persons, 0);
    vector<vector<int> > temp;

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
            cur_ret = deal(temp, surp_nuber, lower_score);
            max_ret = (cur_ret > max_ret) ? cur_ret : max_ret;
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

        ret = get_all_z(persons, scores, surp_nuber, lower_score);
        cout << "Case #" << t << ": " << ret << endl;
    }

	return 0;    
}
