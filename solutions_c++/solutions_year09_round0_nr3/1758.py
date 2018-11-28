    #include<fstream.h>
    #include<iostream.h>
    #include<conio.h>
    #include<string.h>
    #include<math.h>

    char search[]="welcome to code jam";
    int level,count;
    char data[31];

    void recurse(int a)
    {
	int mylevel=level,i;
	int length=strlen(data);
	int flag=0;
	for(i=a;i<length;i++)
	{
	    if(search[mylevel]==data[i])
	    {
		flag=1;
		if(mylevel==18)
		{
		    count++;
		    if(count==10000)
			count=0;
		}
		else
		{
		level=mylevel+1;
		recurse(i+1);
		}
	    }
	}
    }



    void main()
    {
	clrscr();

	int i,m,n;

	fstream fin,fout;
	fin.open("input.txt",ios::in);
	fout.open("output.txt",ios::out);

	fin>>n;

	fin.getline(data,32);
	for(m=1;m<=n;m++)
	{
	fin.getline(data,32);
	level=0;
	count=0;
	recurse(0);
	fout<<"Case #"<<m<<": ";
	if(count<10)
	fout<<"000";
	else if(count<100)
	fout<<"00";
	else if(count<1000)
	fout<<"0";

	fout<<count<<endl;

	}
    fin.close();
    fout.close();

	getch();

    }
