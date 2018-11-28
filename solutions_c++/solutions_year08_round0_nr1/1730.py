#include <iostream>
#include <list>
#include <string>
#include "Parser.h"
#include "Creator.h"
#include "Resolver.h"

int main()
{
	try
	{
		Parser *parser = new Parser();
		Creator *creator = new Creator();	

		Resolver *resolver = new Resolver();

		parseData data;
		std::list<std::string> result;

		std::cout << "Parser Init" << std::endl;
		parser->init("test");
		std::cout << "Parser parse" << std::endl;
		parser->parse(&data, " ");
		std::cout << "Alien Init" << std::endl;
		resolver->init(&data, &result);
		std::cout << "Alien Resolve" << std::endl;
		resolver->resolve();
		std::cout << "Creator Init" << std::endl;
		creator->init("out2");
		std::cout << "Creator Create" << std::endl;
		creator->create(result, "Case #", ": ");
	}
	catch (char *str)
	{
		std::cout << str << std::endl;
		system("pause");
	}
	system("pause");
}