#include <iostream>
#include <string>

using namespace std;

int main()
{
	string res[31] = {"0", "005", "027", "143", "751", "935",
							"607", "903", "991", "335", "047",
							"943", "471", "055", "447", "463",
							"991", "095", "607", "263", "151",
							"855", "527", "743", "351", "135",
							"407", "903", "791", "135", "647"};
	int T;
	cin >> T;
	for (int casenum = 1; casenum <= T; casenum++)
	{
		int n;
		cin >> n;
		cout << "Case #" << casenum << ": " << res[n] << endl;	
	}
	return 0;
}

/*
bash script:
bc
scale=50
base=3+sqrt(5)
i=1
while(i<=30){
	base^i
	i++
}
              	
005		  943 	 	855
027		  471 	 	527
143		  055 	 	743
751		  447 	 	351
935		  463 	 	135
    	      	 
607		  991 	 	407
903		  095 	 	903
991		  607 	 	791
335		  263 	 	135
047		  151 	 	647














*/