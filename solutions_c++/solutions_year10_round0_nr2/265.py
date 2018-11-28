#include <stdio.h>
#include <string.h>
#define MAX_N 1111
#define SIZE 77

int T,N;

class INT
{
	int D[SIZE];
public:
	INT();
	INT(char []);
	INT operator +(INT);
	INT operator -(INT);
	INT operator *(INT);
	INT operator /(INT);
	INT operator %(INT);
	bool operator ==(INT);
	bool operator !=(INT);
	bool operator >(INT);
	bool operator <(INT);
	bool operator >=(INT);
	bool operator <=(INT);
	void PRINT();
};

INT::INT()
{
	int i;
	for (i=0;i<SIZE;i++) D[i] = 0;
}

INT::INT(char S[])
{
	int i,l=strlen(S);
	for (i=0;i<SIZE;i++) D[i] = 0;
	for (i=0;i<l;i++) D[l-i-1] = S[i] - '0';
}

INT INT::operator +(INT V)
{
	int i; INT T;
	
	for (i=0;i<SIZE;i++){
		T.D[i] += D[i] + V.D[i];
		T.D[i+1] += T.D[i] / 10;
		T.D[i] %= 10;
	}

	return T;
}

INT INT::operator -(INT V)
{
	int i; INT T,U;
	
	if ((*this) > V) U = (*this); 
	else{U = V; V = (*this);}

	for (i=0;i<SIZE;i++){
		if (U.D[i] < V.D[i]){
			U.D[i] += 10; U.D[i+1]--;
		}
		T.D[i] = U.D[i] - V.D[i]; 
	}

	return T;
}

INT INT::operator *(INT V)
{
	int i,j; INT T;
	
	for (i=SIZE-1;i>=0;i--){
		if (D[i] == 0) continue;
		for (j=SIZE-1;j>=0;j--){
			if (V.D[j] == 0) continue;
			T.D[i+j] += D[i] * V.D[j];
		}
	}

	for (i=0;i<SIZE-1;i++){
		T.D[i+1] += T.D[i] / 10;
		T.D[i] %= 10;
	}

	return T;
}

INT INT::operator /(INT V)
{
	int l=1; INT T,U = (*this),SS,SV; char S[SIZE] = "1";
	
	for (;;){
		if (INT(S) * V > U) break;
		S[l] = '0'; S[l+1] = '\0'; l++;
	}

	for (;;){
		if (l == 1) break;
		S[--l] = '\0';

		SS = INT(S); SV = SS * V;
		while (1){
			if (SV > U) break;
			T = T + SS;
			U = U - SV;
		}
	}

	return T;
}

INT INT::operator %(INT V)
{
	return (*this) - ((*this)/V)*V;
}

bool INT::operator ==(INT V)
{
	int i;
	for (i=0;i<SIZE;i++) if (D[i] != V.D[i]) return false;
	return true;
}

bool INT::operator !=(INT V)
{
	return !((*this) == V);
}

bool INT::operator >(INT V)
{
	int i;
	for (i=SIZE-1;i>=0;i--){
		if (D[i] != V.D[i]) return D[i] > V.D[i];
	}

	return false;
}

bool INT::operator <(INT V)
{
	return V > (*this);
}

bool INT::operator >=(INT V)
{
	int i;
	for (i=SIZE-1;i>=0;i--){
		if (D[i] != V.D[i]) return D[i] > V.D[i];
	}

	return true;
}

bool INT::operator <=(INT V)
{
	return V >= (*this);
}

void INT::PRINT()
{
	int i;
	for (i=SIZE-1;i>=0;i--) if (D[i] != 0) break;
	if (i == -1){printf ("0"); return;}
	for (i;i>=0;i--) printf ("%d",D[i]);
}

INT GCD(INT A, INT B)
{
	if (B == INT("0")) return A;
	return GCD(B,A%B);
}

char S[SIZE];
INT A,B,G,P;
int C;

int main()
{
	freopen ("B.in","r",stdin);
	freopen ("B.out","w",stdout);

	scanf ("%d",&T);
	while (T--){
		scanf ("%d %s",&N,&S); A = INT(S);
		scanf ("%s",&S); B = INT(S);
		G = A - B;
		for (int i=2;i<N;i++){
			scanf ("%s",&S); B = INT(S); G = GCD(G,B-A);
		} P = (G - A % G) % G;

		printf ("Case #%d: ",++C);
		P.PRINT();
		printf ("\n");
	}

	return 0;
}
