#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct RevCmp
{
	bool operator()(const int& i1, const int& i2) const
	{
		return i1 > i2;
	}
};


int main()
{
    int n;
    cin >> n;
    for (int i = 1; i <= n; i++)
    {
        int dim, tmp;
        cin >> dim;
        vector<int> v1, v2;
        for (int j = 0; j < dim; j++)
        {
            cin >> tmp;
            v1.push_back(tmp);
        }
        for (int j = 0; j < dim; j++)
        {
            cin >> tmp;
            v2.push_back(tmp);
        }
        sort(v1.begin(), v1.end());
        sort(v2.begin(), v2.end(), RevCmp());
        int prod = 0;
        for (int j = 0; j < v1.size(); j++)
            prod+= v1[j] * v2[j];
        cout << "Case #" << i << ": " << prod << endl;
    }
}
