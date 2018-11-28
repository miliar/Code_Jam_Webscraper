#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

#define Max 1000

struct line {
	int i;
	int A;
	int B;
};

bool compA(struct line& L1, struct line& L2)
{
	return L1.A < L2.A;
}

bool compB(struct line& L1, struct line& L2)
{
	return L1.B < L2.B;
}

struct line byA[Max];
struct line byB[Max];
struct line orig[Max];

int findrank(int B, int start, int end)
{
	if(start == end)
		return start;
	if(start+1 == end) {
		if (byB[start].B ==B)
			return start;
		else
			return end;
	}
	int mid = (start+end)/2;
	if(byB[mid].B==B)
		return mid;
	else if(byB[mid].B<B) {
		return findrank(B, mid, end);
	}
	else 
		return findrank(B, start, mid);
}

int main()
{
	//freopen("D:\\tmp\\test.txt","r",stdin);freopen("D:\\tmp\\test.out","w",stdout);
	freopen("D:\\tmp\\A-small.in","r",stdin);freopen("D:\\tmp\\A-small.out","w",stdout);
	//freopen("D:\\tmp\\A-large.in","r",stdin);freopen("D:\\tmp\\A-large.out","w",stdout);
	int testcase;
	cin >> testcase;
	for (int caseId=1;caseId<=testcase;caseId++)
	{
		int N;
		cin >> N;
		int A, B;
		for(int i=0; i<N; i++) {
			cin >> A >> B;
			byA[i].i = i;
			byA[i].A = A;
			byA[i].B = B;
			byB[i] = byA[i];
			orig[i] = byA[i];
		}
		sort(byA, byA+N, compA);
		sort(byB, byB+N, compB);
		int count = 0;
		int rank;
		for(int i=0; i<N; i++) {
			rank = findrank(orig[byA[i].i].B, 0, N-1);
			if(rank > i)
				count += rank-i;
		}
		printf("Case #%d: ",caseId);
		printf("%d", count);
		printf("\n");
		fflush(stdout);
	}

	return 0;
}