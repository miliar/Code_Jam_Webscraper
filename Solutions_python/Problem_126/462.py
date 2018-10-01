object worksheet {

  val data = scala.io.Source.fromFile("/home/james/Downloads/A-small-attempt0.in")
                                                  //> data  : scala.io.BufferedSource = non-empty iterator
  val lines = data.getLines.toList                //> lines  : List[String] = List(100, quartz 3, straight 3, gcj 2, tsetse 2, aka
                                                  //| djaogvoeoueoouxuvxumueiaaaboaaebthmxizmooxeezdluxgbliilaoio 4, ioeuuuoaaeoou
                                                  //| ooalfaouueaeaoioeuiuaeueieuoeuuaiuiiaiueuuieoaeueouuiaiuoeuaaoiuauuaeoeiuaoi
                                                  //| iuuuaaaiaio 2, ieacdeecgudqeuisoqimsfcuexseftudoaitoaoheyuwuduuuouuitaa 2, p
                                                  //| ackmyboxwithfivedozenliquorjugs 1, bweocuuuieuzdnkzmeeiaalesoaijcfeapuydzaav
                                                  //| uyandtowoikoludtuhbhogzyevenliuliqyterauisodv 3, zwuhpnueuaenauuvveajcuciqza
                                                  //| wrvopuuieiooeaujeaxjijjjkeuqbgdwwomaddabfodeuifjizueeeomoiexelamubvdbs 3, pl
                                                  //| gbnvjvycyixxentvhouqkpfsrrgyrvuivrlzhdxqrswwdknhytgfgkttyxllrudjblafpqfbszws
                                                  //| ifzqybdzlysdrbmgpplnzu 9, rpotaeieuutcgaquamniugdobeqxotlkagoapaiuegygpvjfat
                                                  //| auetxzmuahncitoipi 4, uiaaisamkiyaqudaooztceeiuewiuoootomriyuvlvdkiuzalwaono
                                                  //| iuu 4, zgenrqgkottjwsixwqnnkgnwqwetstkpwszhrbrxvgflyohnntqewnlvhbmwrthkiarwd
                                                  //| gsyjydaklsvqnkvqtmdtwzfkcnsgqmg 9, eoeaooaeeauiiuueooiuuoooiaooeeuueiauiiaau
                                                  //| eooauaauiaoaoioeaeuiiuoi
                                                  //| Output exceeds cutoff limit.
  val numberOfCases = lines.head.toInt            //> numberOfCases  : Int = 100
  val caseEntries = lines.tail                    //> caseEntries  : List[String] = List(quartz 3, straight 3, gcj 2, tsetse 2, ak
                                                  //| adjaogvoeoueoouxuvxumueiaaaboaaebthmxizmooxeezdluxgbliilaoio 4, ioeuuuoaaeoo
                                                  //| uooalfaouueaeaoioeuiuaeueieuoeuuaiuiiaiueuuieoaeueouuiaiuoeuaaoiuauuaeoeiuao
                                                  //| iiuuuaaaiaio 2, ieacdeecgudqeuisoqimsfcuexseftudoaitoaoheyuwuduuuouuitaa 2, 
                                                  //| packmyboxwithfivedozenliquorjugs 1, bweocuuuieuzdnkzmeeiaalesoaijcfeapuydzaa
                                                  //| vuyandtowoikoludtuhbhogzyevenliuliqyterauisodv 3, zwuhpnueuaenauuvveajcuciqz
                                                  //| awrvopuuieiooeaujeaxjijjjkeuqbgdwwomaddabfodeuifjizueeeomoiexelamubvdbs 3, p
                                                  //| lgbnvjvycyixxentvhouqkpfsrrgyrvuivrlzhdxqrswwdknhytgfgkttyxllrudjblafpqfbszw
                                                  //| sifzqybdzlysdrbmgpplnzu 9, rpotaeieuutcgaquamniugdobeqxotlkagoapaiuegygpvjfa
                                                  //| tauetxzmuahncitoipi 4, uiaaisamkiyaqudaooztceeiuewiuoootomriyuvlvdkiuzalwaon
                                                  //| oiuu 4, zgenrqgkottjwsixwqnnkgnwqwetstkpwszhrbrxvgflyohnntqewnlvhbmwrthkiarw
                                                  //| dgsyjydaklsvqnkvqtmdtwzfkcnsgqmg 9, eoeaooaeeauiiuueooiuuoooiaooeeuueiauiiaa
                                                  //| ueooauaauiaoaoioeaeuiiuo
                                                  //| Output exceeds cutoff limit.
  
  
  def getSubstrings(input:String):List[String] = {
      (for(i<-0.to(input.length-1);j<-1.to(input.length-i)) yield {input.substring(i,j+i)}).toList
  }                                               //> getSubstrings: (input: String)List[String]
  

  def processEntry(s: String, n: Int): Int = {
    val vowels = List('a', 'e', 'i', 'o', 'u')
    val allSubStrings=getSubstrings(s)
    //println(allSubStrings)
    val matchString=".*([b-df-hj-np-tv-z]){" + n + ",}.*"
		val filtered=allSubStrings.filter(s=>s.matches(matchString))
		//println(filtered)
		//println(filtered.length)
    filtered.length
  }                                               //> processEntry: (s: String, n: Int)Int

  val results=caseEntries.map(_.split(" ")).map(e => processEntry(e(0), e(1).toInt))
                                                  //> results  : List[Int] = List(4, 11, 3, 11, 1027, 1411, 1129, 516, 3148, 3463,
                                                  //|  3901, 1182, 614, 3893, 1064, 1662, 0, 1020, 0, 1982, 1010, 3171, 1938, 3957
                                                  //| , 741, 372, 2194, 216, 3929, 3617, 1470, 1404, 0, 0, 1, 1341, 3073, 959, 385
                                                  //| 7, 3782, 2049, 3736, 1422, 2561, 1508, 245, 2886, 1322, 3165, 891, 807, 1, 9
                                                  //| 20, 714, 2327, 2933, 0, 1134, 2767, 2838, 1196, 473, 2546, 1710, 1674, 785, 
                                                  //| 3799, 557, 772, 1754, 683, 2012, 660, 2262, 2684, 909, 0, 1728, 3151, 0, 335
                                                  //| 1, 5050, 396, 4230, 4442, 1033, 1726, 1339, 3311, 2249, 836, 669, 0, 751, 10
                                                  //| 40, 1056, 1782, 780, 1457, 0)
                                                  
  import java.io.PrintWriter
	import java.io.File
	val pw = new PrintWriter(new File("/home/james/out.txt"))
                                                  //> pw  : java.io.PrintWriter = java.io.PrintWriter@186768e
	
	for(i<-0.to(results.size-1)) {
		pw.println("Case #" + (i+1) + ": " + results(i))
	}
	
  
  pw.close()
                                                  
                                                  

}