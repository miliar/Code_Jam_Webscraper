// ViszinisA

#include <fstream>
#include <iostream>
#include <string>
using namespace std;

class aword {
	public:
		aword *prev, *next;
		char a[15];

		aword (char ta[]) {
			prev = next = NULL;
			strcpy (a, ta);
		}
		
		~aword (){
			delete next;
        }
};

string s[15];
aword *first_word = NULL, *last_word = NULL;
int l, d, n, counta;

int afind(string zis) {
    char caa[15] = {};
    for (int j=0; j<l; j++) {
        caa[j] = zis[j];
    }
	aword *curr = first_word;
	while (strcmp (curr->a,caa)!=0)
	{
		//cout << curr->a << " == " << caa << endl;
		curr = curr->next;
		if (curr==NULL) return 0;
	}
	return 1;
};


void process ()
{
	aword *curr = first_word;
	int i,j;
	bool out=false;

	while (curr!=NULL)
	{
		for (i=0; i<l; i++)
		{
			out = true;
			for (j=0; j<s[i].length(); j++)
			{
				if (curr->a[i]==s[i][j]) {
					out = false;
					break;
				}
			}
			if (out) {
				break;
			}
		}
		if (!out) {
			counta++;
		}
		curr = curr->next;
	}
};

int main ()
{
	FILE * pfin, * pfout;
	pfin = fopen ("a.in", "r");
	pfout = fopen ("a.out", "w");

	aword *tmp = NULL, *curr = NULL;
	int i,j,pos;
	bool inside=false;
	char w[15],c;

	fscanf (pfin, "%d %d %d\n", &l, &d, &n);

	for (i=0; i<d; i++)
	{
		fscanf (pfin, "%s\n", &w);
		
        tmp = new aword(w);
		curr = first_word;
		if (curr==NULL)
		{
			first_word = last_word = tmp;
		} else {
			while (strcmp (w,curr->a)>=0)
			{
				curr = curr->next;
				if (curr==NULL) break;
			}
			if (curr==NULL)
			{
				last_word->next = tmp;
				tmp->prev = last_word;
				last_word = tmp;
			} else {
				tmp->prev = curr->prev;
				tmp->next = curr;

				if (curr->prev!=NULL)
				{
					curr->prev->next = tmp;
				} else {
                       first_word = tmp;
                       }
				curr->prev = tmp;
			}
		}
		
	}
	
	for (i=0; i<n; i++)
	{
		if (i>0)
		{
			fprintf (pfout, "\n");
		}
		for (j=0; j<l; j++)
		{
			s[j] = "";
		}
		pos = 0;
		do
		{
			c = fgetc (pfin);
			if (c == '\n') {
				break;
			}
			if (c == '(') {
				inside = true;
			} else if (c == ')') {
				inside = false;
				pos++;
			} else {
				s[pos] += c;
				if (!inside) {
					pos++;
				}
			}
		} while (c != EOF);
		counta = 0;
		process ();
		//cout << "Case #" << i+1 << ":" << counta;
		fprintf (pfout, "Case #%d: %d",i+1,counta);
	}
	
	delete first_word;

	fclose (pfin);
	fclose (pfout);
	system ("Pause");
	return 0;
}
