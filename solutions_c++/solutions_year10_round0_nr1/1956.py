#include <iostream>
#include <string>

using namespace std;
int N;
int K;
unsigned int SnapperState;

bool ProcessCase()
{
	/*
	urutan SnapperState: 00, 10, 01, 11, 001, 101, 011, 111, ...
	(sama dgn urutan bilangan biner, tapi dgn posisi terbalik (dari LSB ke MSB)
	*/
	SnapperState = K;
	// lampu hanya akan ON jika semua bit di dalam SnapperState bernilai 1,
	// atau SnapperState == 000...0111...1, yaitu dari bit ke-0 sampai bit ke-(N-1) 
	// semuanya '1' (asumsikan bit ke-0 di posisi paling kanan)
	/* jadi, caranya adalah:
		deteksi dari bit ke-0 sampai bit ke-(N-1), apakah ada bit yg bernilai '0'?
		jika ya: OFF, jika tdk: ON.
		Cara:
		tentukan variabel detektor berisi nilai '000...0111...1' (N bit terakhir bernilai '1').
		lalu lakukan operasi: SnapperState & detektor (bitwise AND).
		jika semua bit di dlm SnapperState == '1', maka hasilnya akan sama dgn detektor.
		jika ada bit di dlm SnapperState == '0', maka hasilnya akan tdk sama dgn detektor.
	*/
	unsigned int detektor = 0xFFFFFFFF;
	detektor = detektor << N;
	detektor = ~detektor;	// complement
	if ((SnapperState & detektor) == detektor)
		return true;
	else
		return false;
}

int main()
{
#ifdef SN_INPUT_FILE
	string file1;
	string file2;
	//string file1 = "e:\\test_input - GCJ01.txt";
	//file1 = "e:\\test_input1.txt";
	//file1 = "e:\\C-large-practice.in";
	//file1 = "e:\\C-small-practice.in";
	file1 = "e:\\A-small-attempt0.in";
	//file1 = "e:\\A-large.in";
	FILE * ps;
	freopen_s(&ps, file1.c_str(), "rt", stdin);
	// uncomment for file output:
	//file2 = "e:\\C-large-practice.out";
	//file2 = "e:\\C-small-practice.out";
	file2 = "e:\\A-small-attempt0.out";
	//file2 = "e:\\A-large.out";
	freopen_s(&ps, file2.c_str(), "wt", stdout);
#endif
	bool answer;
	int nCases;
	int caseNumber;
	cin >> nCases;
	string s;
	for (int i=0; i<nCases; i++)
	{
		caseNumber = i+1;
		cin >> N;
		cin >> K;
		answer = ProcessCase();
		cout << "Case #" << caseNumber << ": ";
		if (answer)
			cout << "ON" << endl;
		else
			cout << "OFF" << endl;
	}
	//cout << "press any key to continue..." << endl; _getch();
	return 0;

}
