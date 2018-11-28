#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <cstdlib>

using namespace std;

typedef vector<int> triple;
typedef vector<int> array;

int emax(triple a)
{
    auto res=a[0];
    for (auto i:a)
        if (i>res)
            res=i;
    return res;
}

int emin(triple a)
{
    auto res=a[0];
    for (auto i:a)
        if (i<res)
            res=i;
    return res;
}

int maxCount(triple a)
{
    auto res=0;
    auto maxEl=emax(a);
    for (auto i:a)
        if (i==maxEl)
            res++;
    return res;
}

triple getBestComb(int num)
{
    triple res;
    int k=num/3;
    res.push_back(k);
    int ost=num-k;
    k=ost/2;
    res.push_back(k);
    res.push_back(num-res[0]-res[1]);
    //for (auto i:res)
    //    cout << i << " ";
    //cout << "\n";
    return res;
}

void enlarge(triple &a)
{
    int max=emax(a);
    if (max==0) return;
    if (max==10) return;
    for (auto &i:a)
        if (i==max)
        {
            i++;
            break;
        }
    for (auto &i:a)
        if (i==max)
        {
            i--;
            break;
        }
}

void enlarge2(triple &a)
{
    auto min=emin(a);
    if (min==0) return;
    if (min==10) return;
    for (auto &i:a)
        if (i==min)
        {
            i++;
            break;
        }
    for (auto &i:a)
        if (i==min)
        {
            i--;
            break;
        }
}

triple getBestCombSurpr(int num)
{
    auto res=getBestComb(num);
    if (maxCount(res)>=2)
        enlarge(res);
    else
        enlarge2(res);
    return res;
}

int getBest(int num)
{
    return emax(getBestComb(num));
}

int getBestSurp(int num)
{
    return emax(getBestCombSurpr(num));;
}

array split(string nums)
{
    array res;
    string tmp;
    for (auto c:nums)
        if ((c>='0') && (c<='9'))
            tmp+=c;
        else
            {
                res.push_back(atoi(tmp.c_str()));
                tmp.clear();
            }
    if (tmp.length()>0)
        res.push_back(atoi(tmp.c_str()));
    return res;
}

int main()
{
    string tmp;
    int count;
    int dancers;
    int surprises;
    int maxRes;
    int answ;
    array nums;
    ifstream in("B-large.in");
    ofstream out("output.txt");
    getline(in,tmp);
    count=atoi(tmp.c_str());
    for (auto i=0;i<count;i++)
    {
        //cout << "\nCase " << i+1 << "\n";
        getline(in,tmp);
        if (tmp.length()==0) continue;
        nums=split(tmp);
        if (nums.size()<3) continue;
        dancers=nums[0];
        surprises=nums[1];
        maxRes=nums[2];
        answ=0;
        for (auto j=3;j<3+dancers;j++)
        {
            auto curDancer=nums[j];
            //cout << "Cur dancer: "<< curDancer << "\n";
            if (getBest(curDancer)>=maxRes) answ++;

            else if ((surprises>0) && (getBestSurp(curDancer)>=maxRes))
            {
                answ++;
                surprises--;
            }

        }
        cout << "Case #" << i+1 << ": " << answ << "\n";
        out << "Case #" << i+1 << ": " << answ << "\n";
    }
    in.close();
    out.close();
    return 0;
}
