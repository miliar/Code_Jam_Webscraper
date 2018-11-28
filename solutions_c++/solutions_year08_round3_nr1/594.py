#include <fstream>
#include <vector>
#include <cstdlib>
#include <iostream>

using namespace std;

int findIndex(vector <int> array, int value)
{
    for(int i=0; i<array.size(); i++) if(array[i]==value) return i;
    return -1;
}

void QuickSortWithIndexes(vector <int> &numbers, vector <int> &otherarray, int left, int right)
{
    int pivot, l_hold, r_hold;
    l_hold=left;
    r_hold=right;
    pivot=numbers[left];
    int otherpivot=otherarray[left];
    while(left<right)
    {
        while((numbers[right]>=pivot) && (left<right)) right--;
        if(left!=right)
        {
            numbers[left]=numbers[right];
            otherarray[left]=otherarray[right];
            left++;
        }
        while((numbers[left]<=pivot) && (left<right)) left++;
        if(left!=right)
        {
            numbers[right]=numbers[left];
            otherarray[right]=otherarray[left];
            right--;
        }
    }
    numbers[left]=pivot;
    otherarray[left]=otherpivot;
    pivot=left;
    left=l_hold;
    right=r_hold;
    if(left<pivot) QuickSortWithIndexes(numbers, otherarray, left, pivot-1);
    if(right>pivot) QuickSortWithIndexes(numbers, otherarray, pivot+1, right);
}

int main(void)
{
    ifstream fin("A-input.in");
    ofstream fout("A-output.out");
    int N;
    int P, K, L;
    fin >> N;
    for(int i=1; i<=N; i++)
    {
        fin >> P >> K >> L;
        vector <vector <int> > keys;
        vector <int> letters;
        long long ret=0;
        for(int j=0; j<L; j++)
        {
            int next;
            fin >> next;
            letters.push_back(next);
        }
        int last=0;
        for(int j=0; j<P; j++)
        {
            vector <int> key;
            vector <int> temp=letters;
            vector <int> indexes;
            for(int k=0; k<temp.size(); k++) indexes.push_back(k);
            QuickSortWithIndexes(temp, indexes, 0, temp.size()-1);
            reverse(temp.begin(), temp.end());
            reverse(indexes.begin(), indexes.end());
            for(int k=last; (k<temp.size()) && (key.size()<K); k++)
            {
                key.push_back(indexes[k]);
                last=k;
            }
            last++;
            keys.push_back(key);
        }
        for(int j=0; j<letters.size(); j++) for(int k=0; k<keys.size(); k++) if(findIndex(keys[k], j)!=-1)
        {
            ret+=letters[j]*(k+1);
            break;
        }
        fout << "Case #" << i << ": " << ret << endl;
    }
    fin.close();
    fout.close();
    return 0;
}
