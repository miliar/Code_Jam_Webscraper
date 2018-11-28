/*
* Start time: 13:51, 2209-08-24
*/
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <set>
//#include <map>

using namespace std;

string convert(int n)
{
	static string c="";
	if(n<10)
	{
		c=(char)(n%10+'0');
		return c;
	}
	else
	{
		c=convert(n/10)+(char)(n%10+'0');
		return c;
	}
}


//const string desStr="welcome to code jam";
//
//string::size_type findChar(char c, int start, int end)
//{
//	for(string::size_type index=start+1; ; index != end; ++index)
//	{
//		if(message[index0] == c)
//			return 	index;
//		else
//			continue;
//	}
//}
//
//int findLast(int start)
//{
//	for(string::size_type index=start; ; index != message.size; ++index)
//	{
//		if(message[index0] == 'm')
//		{
//			++welcomeCount;
//			if(welcomeCount>100000)
//				welcomeCount=welcomeCount%10000;
//			return 	welcomeCount;
//		}
//		else
//			continue;
//	}
//}
int main(void)
{
	string InFileName="C-small-attempt1.in";
	string OutFileName="C-small-attempt1.out";

	ifstream fin;
	ofstream fout;

	//open input file
	fin.open(InFileName.c_str(), ios::in);
	if(fin.fail())
	{
		std::cerr<<"Input file open error!";
	}

	//create output file
	fout.open(OutFileName.c_str(), ios::out);	
	if(fout.fail())
	{
		std::cerr<<"Output file open error!";
	}

	int caseNum=0;
	int caseCount=1;
	fin>>caseNum;
	fin.ignore(1,'\n');

	while(caseCount<=caseNum)//for case loop
	{
		int welcomeCount=0;

		string message;
		getline(fin, message, '\n');

		int length = message.size();

		//string::size_type index = 0£»
		//for(; index != desStr.size; ++index)
		//{
		//	findChar(desStr[index], , length-(18-index));
		//}
		//int pos = -1;
		//   int start=	findChar('w', pos, length-(18-index));

		//string::size_type findChar(char c, int start, int end)
		int size= message.size();
		if(size>=19)
		{

			for(string::size_type index0=0; index0 != size - 18; ++index0)
			{
				if(message[index0] != 'w')
					continue;
				for(string::size_type index1=index0+1; index1 != size - 17; ++index1)
				{
					if(message[index1] != 'e')
						continue;
					for(string::size_type index2=index1+1; index2 != size - 16; ++index2)
					{
						if(message[index2] != 'l')
							continue;

						for(string::size_type index3=index2+1; index3 != size - 15; ++index3)
						{
							if(message[index3] != 'c')
								continue;
							for(string::size_type index4=index3+1; index4 != size - 14; ++index4)
							{
								if(message[index4] != 'o')
									continue;

								for(string::size_type index5=index4+1; index5 != size - 13; ++index5)
								{
									if(message[index5] != 'm')
										continue;
									for(string::size_type index6=index5+1; index6 != size - 12; ++index6)
									{
										if(message[index6] != 'e')
											continue;
										for(string::size_type index7=index6+1; index7 != size - 11; ++index7)
										{
											if(message[index7] != ' ')
												continue;
											for(string::size_type index8=index7+1; index8 != size - 10; ++index8)
											{
												if(message[index8] != 't')
													continue;
												for(string::size_type index9=index8+1; index9 != size - 9; ++index9)
												{
													if(message[index9] != 'o')
														continue;
													for(string::size_type index10=index9+1; index10 != size - 8; ++index10)
													{
														if(message[index10] != ' ')
															continue;
														for(string::size_type index11=index10+1; index11 != size - 7; ++index11)
														{
															if(message[index11] != 'c')
																continue;

															for(string::size_type index12=index11+1; index12 != size - 6; ++index12)
															{
																if(message[index12] != 'o')
																	continue;
																for(string::size_type index13=index12+1; index13 != size - 5; ++index13)
																{
																	if(message[index13] != 'd')
																		continue;
																	for(string::size_type index14=index13+1; index14 != size - 4; ++index14)
																	{
																		if(message[index14] != 'e')
																			continue;
																		for(string::size_type index15=index14+1; index15 != size - 3; ++index15)
																		{
																			if(message[index15] != ' ')
																				continue;
																			for(string::size_type index16=index15+1; index16 != size - 2; ++index16)
																			{
																				if(message[index16] != 'j')
																					continue;
																				for(string::size_type index17=index16+1; index17 != size - 1; ++index17)
																				{
																					if(message[index17] != 'a')
																						continue;

																					for(string::size_type index18=index17+1; index18 != size; ++index18)
																					{
																						if(message[index18] == 'm')
																						{
																							++welcomeCount;
																							if(welcomeCount>100000)
																								welcomeCount=welcomeCount%10000;
																						}
																						else
																							continue;

																					}
																					continue;

																				}

																			}

																		}

																	}

																}

															}
														}

													}

												}

											}

										}

									}

								}
							}
						}
					}
				}

			}
		}
		string countStr="";
		countStr+=convert(welcomeCount);

		if(welcomeCount<1000)
			countStr='0'+countStr;
		if(welcomeCount<100)
			countStr='0'+countStr;
		if(welcomeCount<10)
			countStr='0'+countStr;
		fout<<"Case #"<<caseCount++<<": "<<countStr<<'\n';
	}


	//close input file& output file
	fin.close();
	fout.close();

	return 1;
}