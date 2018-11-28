
#include<iostream>
#include<fstream.h>
#include<string>

int main()
{
	int i, j, tc,len;

	ifstream inf("input.in");
   ofstream opf("one.o");

   inf>>tc;
   char str[102], ans[102];
   inf.getline(str,101);
   for(i=0 ; i<tc ; i++)
   {
                  opf<<"Case #"<<(i+1)<<": ";
              	inf.getline(str,101);
              	len=strlen(str);
              	for(j=0 ; j<len ; j++)
              	{
                        switch(str[j])
                        {
                                         case 'y': ans[j]='a';
                                              break;
                                              
                                         case 'n': ans[j]='b';
                                              break;

                                         case 'f': ans[j]='c';
                                              break;

                                         case 'i': ans[j]='d';
                                              break;

                                         case 'c': ans[j]='e';
                                              break;

                                         case 'w': ans[j]='f';
                                              break;

                                         case 'l': ans[j]='g';
                                              break;

                                         case 'b': ans[j]='h';
                                              break;

                                         case 'k': ans[j]='i';
                                              break;

                                         case 'u': ans[j]='j';
                                              break;

                                         case 'o': ans[j]='k';
                                              break;

                                         case 'm': ans[j]='l';
                                              break;

                                         case 'x': ans[j]='m';
                                              break;

                                         case 's': ans[j]='n';
                                              break;

                                         case 'e': ans[j]='o';
                                              break;

                                         case 'v': ans[j]='p';
                                              break;

                                         case 'z': ans[j]='q';
                                              break;

                                         case 'p': ans[j]='r';
                                              break;

                                         case 'd': ans[j]='s';
                                              break;

                                         case 'r': ans[j]='t';
                                              break;

                                         case 'j': ans[j]='u';
                                              break;

                                         case 'g': ans[j]='v';
                                              break;

                                         case 't': ans[j]='w';
                                              break;

                                         case 'h': ans[j]='x';
                                              break;

                                         case 'a': ans[j]='y';
                                              break;

                                      //   case 'y': ans[j]='a';
                                        //      break;

                                         case 'q': ans[j]='z';
                                              break;
                                              
                                         default: ans[j]=str[j];

                        }
              }
              opf.write(ans,len);
              opf<<"\n";
                
   }
   return 0;
}
