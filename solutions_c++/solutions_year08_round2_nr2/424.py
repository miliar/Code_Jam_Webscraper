#include <stdio.h>
#include <stdlib.h>

#include <string>
#include <vector>
#include <map>
#include <iostream>
#include <algorithm>

#include <math.h>

using namespace std;
#define INF 0x7FFFFFFF

class DisjointSets
{
public:
        long long int* m_pUnionFindStruct;
        long long int num_elements;
        long long int num_disjoint_sets;  // number of disjoint sets
		long long int max;
		long long int A, B;

    DisjointSets();
    ~DisjointSets();
    void init(long long int A, long long int B);
        void MakeSet(long long int no);
        int  Find(long long int x);        // return the canonical name for the set containing x
        void Union(long long int x, long long int y); // union the sets containing x and y
};


void DisjointSets::init(long long int a, long long int b){
	A=a;B=b;
	max=B-A+1;
    m_pUnionFindStruct = new long long int[max];
    num_disjoint_sets = 0;
    num_elements=0;
    for(long long int i=0;i<max;i++)
	{
		MakeSet(A+i);
	}
}

DisjointSets::DisjointSets(){
}

DisjointSets::~DisjointSets(){
    delete [] m_pUnionFindStruct;
}

void DisjointSets::MakeSet(long long int no)
{
    num_elements++;
    num_disjoint_sets++;
    m_pUnionFindStruct[no-A] = -1;
}

int DisjointSets::Find(long long int x)
{
    if(m_pUnionFindStruct[x-A] == INF)
        return -1;
    int j=x,root=x;
    while(m_pUnionFindStruct[j-A]>=0)
        j = m_pUnionFindStruct[j-A];
    root = j;
    while(m_pUnionFindStruct[x-A]>=0){
        j = m_pUnionFindStruct[x-A];
        m_pUnionFindStruct[x-A] = root;
        x = j;
    }
    return root;
}
void DisjointSets::Union(long long int x, long long int y)
{
    long long int root1 = Find(x);
    long long int root2 = Find(y);
    if(root1==root2)
        return;
        if(m_pUnionFindStruct[root2-A]<m_pUnionFindStruct[root1-A]){
        m_pUnionFindStruct[root2-A] += m_pUnionFindStruct[root1-A];
        m_pUnionFindStruct[root1-A] = root2;
    }else{
        m_pUnionFindStruct[root1-A] += m_pUnionFindStruct[root2-A];
                m_pUnionFindStruct[root2-A] = root1;
    }
    num_disjoint_sets--;
}

vector<long long int>  generatePrimes(long long int B)
{
	vector<long long int> v1;
	vector<long long int>::iterator v1_iter;
	v1.push_back(2ll);
	for(long long i=3; i<=B; i++)
	{
		for(v1_iter=v1.begin(); v1_iter!=v1.end(); v1_iter++)
		{
			if(i%(*v1_iter) == 0)
				break;
		}

		if(v1_iter==v1.end())
			v1.push_back(i);
	}
	return v1;
}

int main()
{
	long long int i,j,k,l,m,n;
	int testId, nTests;

	scanf("%d", &nTests);
	for(testId=1;testId<=nTests;testId++)
	{
		//XXX  -- Read input --  XXX
		long long int a, b, p;
		cin >> a >> b >> p;
		DisjointSets d;
		d.init(a,b);

		vector<long long int> primes;
		vector<long long int>::iterator pr_iter;
		//XXX  -- Process input --  XXX
		primes = generatePrimes(b);
		//for(pr_iter=primes.begin();pr_iter!=primes.end();pr_iter++)
		//{
		//	cout << (*pr_iter) << " ";
		//}
		//cout << endl;
		for(pr_iter=primes.begin(); d.num_disjoint_sets>1 && pr_iter!=primes.end();pr_iter++)
		{
			if((*pr_iter)<p)
				continue;
			long long firstNo, no;
			for(no=a;no<=b;no++)
			{
				if(no%(*pr_iter) == 0)
				{
					firstNo=no;
					break;
				}
			}
			for(no++;no<=b;no++)
			{
				if(no%(*pr_iter) == 0)
				{
					d.Union(firstNo, no);
				}
			}
		}

		//XXX  -- Print output --  XXX
		printf("Case #%d: %lld\n",testId, d.num_disjoint_sets);

	}

	return 0;
}
