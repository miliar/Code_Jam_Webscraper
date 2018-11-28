#include <iostream>
#include <vector>

using namespace std;


int main()
{
    int coden, maxn;
    cin >> maxn;
    // define vars
    string temp;
    vector<int> nums;
    vector<int> last;
    int pt;
    int i;
    int size;
    int t;

    for (coden = 1; coden <= maxn; coden++)
    {
        cin >> temp;
        nums.clear();
        last.clear();
        for (i = 0; i < temp.size(); i++)
        {
            nums.push_back(temp[i] - '0');
        }
        /*for (int i = 0; i < nums.size(); i++)
        {
            cout << nums[i];
        }
        cout << endl;
        */
        for (pt = temp.size() - 1; pt > 0; pt--)
        {
            if (nums[pt] > nums[pt-1]) break;
        }
        size = nums.size();

        // output result
        cout << "Case #" << coden << ": ";

        if (pt == 0)
        {
            for (i = size - 1; i >=0; i--)
            {
                if (nums[i] != 0)
                {
                    cout << nums[i];
                    t = i;
                    break;
                }
            }
            cout << '0';
            for (i = size - 1; i >= 0; i--)
            {
                if (i != t)
                    cout << nums[i];
            }
        }
        else
        {
            for (i = 0; i < pt - 1; i++)
            {
                cout << nums[i];
            }
            t = nums[pt - 1];
            bool flag = false;
            for (i = size - 1; i >= pt; i--)
            {
                if (!flag && nums[i] > t)
                {
                    cout << nums[i];
                    flag = true;
                    last.push_back(t);
                }
                else
                    last.push_back(nums[i]);
            }
            for (i = 0; i < last.size(); i++)
            {
                cout << last[i];
            }
        }

        cout << endl;
    }
    return 0;
}

