#include <vector> 
#include <map> 
#include <iostream> 
#include <string> 

using namespace std;

char in_file[] = "B-small-attempt0.in";
char out_file[] = "B-small.out";

map<int, vector<int> > mapper;

void gen_all_nums()
{
    int sum,avg,yu;
    vector<int> tmp;

    mapper[0].push_back(0);
    mapper[0].push_back(0);
    mapper[1].push_back(1);
    mapper[0].push_back(1);

    for (sum=2; sum<=30; sum++)
    {
        avg = sum/3;
        yu  = sum%3;

        if (yu == 1)
        {
            mapper[sum].push_back(avg+1);       //激励解
            mapper[sum].push_back(avg+1);       //非激励解
        }
        else if (yu == 2)
        {
            mapper[sum].push_back(avg+2);       //激励解
            mapper[sum].push_back(avg+1);         //非激励解
        }
        else if (yu == 0)
        {
            mapper[sum].push_back(avg+1);       //激励解
            mapper[sum].push_back(avg);        //非激励解
        }
    }
}

int get_all_z(int persons, vector<int> &scores, int surp_nuber, int lower_score)
{
    int i = 0;
    int jili_count = 0;
    int max_person = 0;
    int index;

    sort(scores.begin(), scores.end());
    for (i=0;i<scores.size() && mapper[scores[i]][0] < lower_score; i++)
        ;

    for (;i<scores.size();i++)
    {
        if (jili_count != surp_nuber)
        {
            jili_count++;
            index = 0;
        }
        else
            index = 1;

        if (mapper[scores[i]][index] >= lower_score)
            max_person++;
    }

    return max_person;
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
