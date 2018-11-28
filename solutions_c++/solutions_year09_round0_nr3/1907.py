#include   <string>  
#include   <iostream>  
#include <fstream>
using namespace std; 
//0

unsigned long lCount = 0;
int count = 0;

int  main()  
{  


    string inStr;  
    ifstream fin("C-small-attempt2.in");  

	getline(fin, inStr);
    while (getline(fin, inStr))
	{
		string::size_type pos1 = 0, pos2,  pos3, pos4, pos5, pos6,
							 pos7, pos8, pos9, pos10, pos11, pos12, pos13,
							  pos14, pos15, pos16, pos17, pos18, pos19;
		while((pos1 = inStr.find_first_of('w', pos1) +1) != 0){
			pos2 = pos1;
			while((pos2 = inStr.find_first_of('e', pos2) +1) != 0){
				pos3 = pos2;
				while((pos3 = inStr.find_first_of('l', pos3) +1) != 0){
					pos4 = pos3;
					while((pos4 = inStr.find_first_of('c', pos4) +1) != 0){
						pos5 = pos4;
						while((pos5 = inStr.find_first_of('o', pos5) +1) != 0){
							pos6 = pos5;
							while((pos6 = inStr.find_first_of('m', pos6) +1) != 0){
								pos7 = pos6;
								while((pos7 = inStr.find_first_of('e', pos7) +1) != 0){
									pos8 = pos7;
									while((pos8 = inStr.find_first_of(' ', pos8) +1) != 0){
										pos9 = pos8;
										while((pos9 = inStr.find_first_of('t', pos9) +1) != 0){
											pos10 = pos9;
											while((pos10 = inStr.find_first_of('o', pos10) +1) != 0){
												pos11 = pos10;
												while((pos11 = inStr.find_first_of(' ', pos11) +1) != 0){
													pos12 = pos11;
													while((pos12 = inStr.find_first_of('c', pos12) +1) != 0){
														pos13 = pos12;
														while((pos13 = inStr.find_first_of('o', pos13)+1) != 0){
															pos14 = pos13;
															while((pos14 = inStr.find_first_of('d', pos14) +1) != 0){
																pos15 = pos14;
																while((pos15 = inStr.find_first_of('e', pos15) +1) != 0){
																	pos16 = pos15;
																	while((pos16 = inStr.find_first_of(' ', pos16) +1) != 0){
																		pos17 = pos16;
																		while((pos17 = inStr.find_first_of('j', pos17) +1) != 0){
																			pos18 = pos17;
																			while((pos18 = inStr.find_first_of('a', pos18) +1) != 0){
																				pos19 = pos18;
																				while((pos19 = inStr.find_first_of('m', pos19) +1) != 0){
																					++lCount;
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
	cout << "Case #"<< ++count << ": ";
	printf("%04ld\n", lCount);
	lCount = 0;



//		string::size_type wPos = inStr.find_first_of('w');
	
	}
	
	

	return 0;
}
