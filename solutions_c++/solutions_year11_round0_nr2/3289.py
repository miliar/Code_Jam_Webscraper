#include <iostream>
#include <fstream>
using namespace std;

void combine_check (char **combine, char *list, const int C, int& list_length);
void oppose_check (char **oppose, char *list, const int D, const int N,
		   int& list_length);

int main()
{
	ifstream input;
	input.open("magicka.in");
	ofstream output;
	output.open("magicka.out");
	int cases;
	input >> cases;
	for (int i = 1; i <= cases; i++) {
		cout << endl << i << ":\ncombine:\n";
		int C, D, N;
		input >> C;
		char **combine;
		if (C > 0) combine = new char*[C];
		for (int j = 0; j < C; j++) {
			*(combine+j) = new char[3];
			input >> *(*(combine+j)) >> *(*(combine+j)+1)
			      >> *(*(combine+j)+2);
			cout << combine[j][0] << ' ' << combine[j][1] << ' '
			      << combine[j][2] << endl;
		}		
		cout << "oppose:\n";
		input >> D;
		char **oppose;
		if (D > 0) oppose = new char*[D];
		for (int j = 0; j < D; j++) {
			*(oppose+j) = new char[2];
			input >> *(*(oppose+j)) >> *(*(oppose+j)+1);
			cout << oppose[j][0] << ' ' << oppose[j][1] << endl;
		}
		cout << "list:\n";
		int list_length = 0;
		input >> N;
		char *list = new char[N];
		for (int j = 0; j < N; j++) {
			input >> *(list + list_length);
			list_length++;
			if (C > 0)
				combine_check(combine, list, C, list_length);
			cout << j << "\t" << *(list+list_length - 1) << endl;
			if (D > 0)
				oppose_check(oppose, list, D, N, list_length);
			cout << j << "\t" << *(list+list_length - 1) << endl;
			cout << "\t" << list_length << endl;
			if(j == 2 && list[0] == 'R' && list[1] == 'I')
				cout << *(list + 2) << endl;
			
		}

		output << "Case #" << i << ": [";
		if (list_length > 0) {
			output << *list;
		}
		for (int j = 1; j < list_length; j++) {
			output << ", " << *(list + j);
		}
		output << ']' << endl;
	}

	return 0;
}


void combine_check (char **combine, char *list, const int C, int& list_length)
{
	bool unfound = true;
	char *ptr1 = NULL;
	char *ptr2 = NULL;
	for(int i = 0; i < C && unfound; i++) {
		ptr1 = list + list_length - 2;
		ptr2 = list + list_length - 1;
		if(((*ptr1 == *(*(combine + i))) && (*ptr2 == *(*(combine + i) + 1))) ||
		   ((*ptr2 == *(*(combine + i))) && (*ptr1 == *(*(combine + i) + 1)))) {
			*(list + list_length - 2) = *(*(combine + i) + 2);
			*(list + list_length - 1) = '0';
			list_length--;
			unfound = false;
		}
	}
	return;
}


void oppose_check (char **oppose, char *list, const int D, const int N,
		   int& list_length)
{
	char check = *(list + list_length - 1);
	for (int i = 0; i < D; i++) {
		if (check == *(*(oppose + i))) {
			for (int j = 0; j < N; j++) {
				if(*(list + j) == *(*(oppose + i) + 1)) {
					for(int k = 0; k < list_length; k++)
						*(list + k) = '0';
					list_length = 0;
					break;
				}
			}
		}
		else if (check == *(*(oppose + i) + 1)) {
			for (int j = 0; j < N; j++) {
				if(*(list + j) == *(*(oppose + i))) {
					for(int k = 0; k < list_length; k++)
						*(list + k) = '0';
					list_length = 0;
					break;
				}
			}
		}
	}	
}

