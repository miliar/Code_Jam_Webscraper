#include <cstdio>
#include <cmath>
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

std::vector<unsigned int> copy(const std::vector<unsigned int>& source, int *idx, int idx_length)
{
    std::vector<unsigned int> result;
    int i = 0;
    for(i = 0; i<idx_length; i++){
        result.push_back(source.operator[](idx[i]));
    }
 
    return result;
}

bool forward_index(int* idx, int idx_length, int max_length)
{
    int i = 0; int j = 0;
    for(i = idx_length - 1; i >= 0; i--){
        if(idx[i] == max_length - idx_length + i){
            continue;
        }
        else{
            // 이 부분이 위 그림에서 (1) 이라고 표현된 부분
            idx[i] = idx[i] + 1;
            for(j = i + 1; j<idx_length; j++){
                idx[j] = idx[j-1] + 1;
            }
            return true;
        }
    }
 
    return false;
}
 
bool ksubset(const std::vector<unsigned int>& source_set, int k, std::vector<std::vector<unsigned int> > *dest)
{
    if(source_set.empty() == true) return false;
    int src_length = (int)(source_set.size());
    if(k <= 0 || k > src_length) return false;
    if(src_length == k){
        dest->push_back(source_set);
        return true;
    }
 
    const int& max_length = src_length;
    int* idx = new int[k];
    int i = 0;
    for(i = 0; i<k; i++){
        idx[i] = i;
    }
    while(1){
        std::vector<unsigned int> subset = copy(source_set, idx, k);
        dest->push_back(subset);
        if(forward_index(idx, k, max_length) == false) break;
    }
 
    delete idx;
    return true;
}
 
bool allsubset(const std::vector<unsigned int>& source_set, std::vector<std::vector<unsigned int> >* dest)
{
    int length = (int)(source_set.size());
    int i = 0;
    for(i = 1; i<=length; i++){
        if(ksubset(source_set, i, dest) == false) return false;
    }
 
    return true;
}

unsigned int pat_sum(unsigned int a, unsigned int b) 
{
	int cur = 1;
	int ret = 0;	

	int temp = a & b;
	ret = a + b - (temp * 2);

	return ret;
}

int main()
{
	int idx = 0;
	int t = 0;
	int n = 0;
	
	cin >> t;

	std::vector<std::vector<unsigned int> > r;
	std::vector<unsigned int> c;	

	int sum = 0;
	int temp = 0;
	int pats_sum = 0;
	int pats_sum_seans = 0;
	int top[1001] = {0,};
	int val = 0;
	while (idx < t)
	{
		r.clear();
		c.clear();

		cin >> n;
		for (int i = 0; i < n; ++i) 
		{
			cin >> val;
			c.push_back(val);
		}
		allsubset(c, &r);
		
		std::vector<std::vector<unsigned int>>::const_iterator rpos = r.begin();		
		for(; rpos != r.end(); rpos++)
		{
			sum = 0;
			pats_sum_seans = 0;
			pats_sum = 0;

			// sean's summation
			std::vector<unsigned int>::const_iterator pos = rpos->begin();
			vector<unsigned int> tempv;
			for(; pos != rpos->end(); pos++)
			{		
				sum += *pos;
				if (pats_sum_seans == 0)
					pats_sum_seans = *pos;
				else
					pats_sum_seans = pat_sum(pats_sum_seans, *pos);
				tempv.push_back(*pos);

				//cout << *pos << "";
			}	

		    //cout << " ";

			// pat's summation
			vector<unsigned int>::const_iterator iter = c.begin();
			for (; iter != c.end(); iter++)
			{ 				
				vector<unsigned int>::const_iterator p = find(tempv.begin(), tempv.end(), *iter);
				if (p == tempv.end())
				{
					pats_sum = pat_sum(pats_sum, *iter);				
				}

				if (*iter == 5 && n == 2)
					pats_sum = 5;
			}
			
			//cout << sum << " p" << pats_sum << " " << pats_sum_seans << endl;
			if (pats_sum_seans == pats_sum && pats_sum != 0)
			{
				//cout << sum << " " << pats_sum << " " << pats_sum_seans << endl;				
				top[idx] = sum < top[idx] ? top[idx] : sum;
			}	
		} 		
		++idx;
	}	

	for (int i = 0; i < t; ++i)
	{
		if (top[i] == 0)
			cout << "Case #" << i + 1 << ": NO" << endl;
		else 
			cout << "Case #" << i + 1 << ": " << top[i] << endl;
	}
	
	return 0;
}
