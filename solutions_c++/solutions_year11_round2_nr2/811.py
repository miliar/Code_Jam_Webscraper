#include<cmath>
#include<iostream>
#include<string>
#include<vector>
#include<cstdlib>
#include<cmath>
#include<map>

using namespace std;

int main()
{
    int t, count;
    cin >> t;
    count=0;
    int c,d;
    double sum, dis;
    double min,temp;
    vector<int> p, v;
    while (count<t)
    {
        count++;
        min=-1;
        cout << "Case #" << count << ": ";
        cin >> c >> d;
        p.clear(); v.clear();
        p.assign(c,0); v.assign(c,0);

        for (int i=0; i<c; i++)
        {
            cin >> p[i] >> v[i];
            if (min==-1 || min<((v[i]-1)*d/2.0))
                min = ((v[i]-1)*d/2.0);
        }

        for (int i=0; i<c; i++)
            for(int j=i+1; j<c; j++)
            {
                sum=0;
                dis=p[j]-p[i];
                for (int k=i; k<=j; k++)
                    sum+=v[k];
                if (((sum-1)*d-dis)/2.0>min)
                    min=((sum-1)*d-dis)/2.0;
            }
        if (min==(int)min)
            cout << min << ".0" << endl;
        else
            cout << min << endl;
    }
    
}
