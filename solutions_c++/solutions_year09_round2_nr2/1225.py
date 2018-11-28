#include <iostream>

int main()
{
	int n;
	std::cin >> n;
	bool done;
	for (int i=0; i<n; i++)
	{
		done = false;
		char buf[30], buf2[30];
		std::cin >> buf;
		strcpy(buf2, buf);
		std::cout << "Case #" << (i+1) << ": ";
		for (int j=strlen(buf)-1; j>0; j--)
		{
			bool thereis = false;
			for (int m=j; m<strlen(buf); m++)
			{
				if (buf[j-1] < buf[m])
					thereis = true;
			}
			if (thereis)
			{
				if (buf[j-1] == '0')
				{
					for (int k=strlen(buf)-1, l=0; k>=j; k--, l++)
						buf[j+l] = buf2[k];
					strcpy(buf2, buf);
					int k,l;
					for (k=0; k<j-1; k++)
							std::cout << buf[k];
					for (k=j, l=0; k<strlen(buf); k++, l++)
					{
						if (buf[k] != '0')
						{
							std::cout << buf[k];
							break;
						}
					}
					strcpy(buf2, &(buf[k+1]));
					for (; l>=0; l--)
						std::cout << "0";
					std::cout << buf2 << std::endl;
					done = true;
					break;
				}
//				buf[j-1] = buf2[j];
//				buf[j] = buf2[j-1];
				for (int k=0; k<j-1; k++)
						std::cout << buf[k];
				for (int l=buf[j-1]+1-48; l<=9; l++)
				{
					for (int k=j-1; k<strlen(buf); k++)
					{
						if (buf[k] == l+48)
						{
							std::cout << buf[k];
							buf[k] = 47;
							goto next;
						}
					}
				}
next:
				for (int l=0; l<=9; l++)
				{
					for (int k=j-1; k<strlen(buf); k++)
					{
						if (buf[k] == l+48)
						{
							std::cout << buf[k];
							buf[k] = 47;
						}
					}
				}
				std::cout << std::endl;
				done = true;
				break;
			}
		}
		if (!done)
		{
			for (int k=strlen(buf)-1, l=0; k>=0; k--, l++)
				buf[l] = buf2[k];
			int k;
			for (k=0; k<strlen(buf); k++)
			{
				if (buf[k] != '0')
				{
					std::cout << buf[k];
					break;
				}
			}
			strcpy(buf2, &(buf[k+1]));
			for (; k>=0; k--)
				std::cout << "0";
			std::cout << buf2 << std::endl;
		}
	}
}
