 #include<iostream>
 
 using namespace std;
 
 int main()
 {	unsigned int TestCases,Googlers,Solution;
	int MinimumMaxScore,TotalScore,SurpriseCases;
	cin>>TestCases;
	for(unsigned int TestCase = 0; TestCase < TestCases; ++TestCase)
	{	cin>>Googlers>>SurpriseCases>>MinimumMaxScore;
		Solution = 0;
		for(unsigned int Googler = 0; Googler < Googlers; ++Googler)
		{	cin>>TotalScore;
			if(TotalScore == 3*MinimumMaxScore - 4 || TotalScore == 3*MinimumMaxScore - 3)  //Verified and proved
			{	if(MinimumMaxScore >=2 && SurpriseCases>0)
				{	SurpriseCases--;
					Solution++;
				}
			}
			else if(TotalScore < 3*MinimumMaxScore - 4)
				;
			else if(TotalScore == 3*MinimumMaxScore - 2 || TotalScore == 3*MinimumMaxScore - 1)
			{	if(MinimumMaxScore >= 1)
					Solution++;
			}
			else Solution++;
		}
		cout<<"Case #"<<TestCase+1<<": "<<Solution<<"\n";
	}
}